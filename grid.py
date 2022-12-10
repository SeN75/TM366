from asyncore import write
import math
import random
import numpy as np

log = open('grid.log.txt', 'w', encoding="utf-8")


def create_grid(col, row):
    cell_value = 1
    grid = []
    result_grid = []
    for x in range(1, col + 1):
        grid.insert(x, [])
        result_grid.insert(x, [])
        for y in range(1, row+1):
            grid[x-1].insert(y, str(cell_value))
            result_grid[x-1].insert(y, '0')
            cell_value += 1
    gird_t = np.array(grid)
    gird_t = gird_t.transpose()
    result_grid_t = np.array(result_grid)
    result_grid_t = result_grid_t.transpose()
    return [gird_t, result_grid_t]


def set_cell(robot, goal, restricted):
    grid = create_grid(7, 7)[0].tolist()
    result_grid = create_grid(7, 7)[1].tolist()
    robot_current_value = "& " + str(grid[robot[1] - 1][robot[0]-1])
    goal_pos = "$ " + grid[goal[1] - 1][goal[0]-1]
    for cell in restricted:
        grid[cell[1]-1][cell[0] - 1] = "X " + grid[cell[1]-1][cell[0] - 1]
        result_grid[cell[1]-1][cell[0] - 1] = "X"

    grid[robot[1] - 1][robot[0]-1] = robot_current_value
    result_grid[robot[1] - 1][robot[0]-1] = '&'
    grid[goal[1] - 1][goal[0]-1] = goal_pos
    result_grid[goal[1] - 1][goal[0]-1] = '$'
    return [grid, result_grid]


def ecludian(point1, point2):
    r = round(math.sqrt(
        math.pow(point1[0] - point2[0], 2) + math.pow(point1[1] - point2[1], 2)), 2)
    log.write("\n√((x1-x2)^2 + (y1-Y2)^2)\n")
    log.write('√(( ' + str(point1[0]) + ' - ' + str(point2[0]) + ' )^2 + ( ' +
              str(point1[1]) + ' - ' + str(point2[1]) + ' ) ^2 ) = ' + str(r))
    print('√((', str(point1[0]), '-', str(point2[0]), ')^2 + (',
          point1[1], '-', point2[1], ')^2) =', r)

    return r


def is_valid_pos(grid, pos):
    cell_value = grid[pos[1] - 1][pos[0]-1]
    if "X " in cell_value:
        return False
    return True


def recod_state(grid, pos, goal, dir):
    new_state = {
        "state": grid[pos[1]-1][pos[0]-1],
        "pos": pos,
        "h": ecludian(goal, pos),
        "dir": dir
    }
    return new_state


def sort_history(history):
    min_idx = 0
    for i in range(len(history)):
        min_idx = i
        chose = random.sample(set('10'), 1)
        for j in range(i+1, len(history)):
            if(chose[0] == '0'):
                if history[min_idx]["h"] >= history[j]["h"]:
                    min_idx = j
            else:
                if history[min_idx]["h"] > history[j]["h"]:
                    min_idx = j
        history[i], history[min_idx] = history[min_idx], history[i]


def start_move():
    robot_pos = [5, 4]
    robot_old_pos = list(robot_pos)
    goal_pos = [3, 5]
    restricted = [[7, 1], [3, 4], [6, 5], [7, 5], [4, 6]]
    history = []

    grid = set_cell(robot_pos, goal_pos, restricted)[0]
    board = set_cell(robot_pos, goal_pos, restricted)[1]
    number_move = 0
    condiation = True
    history.append(recod_state(grid, robot_pos, goal_pos, "S"))
    while(condiation):

        move_up = list(robot_pos)
        move_up[1] = move_up[1] - 1
        move_down = list(robot_pos)
        move_down[1] = move_down[1] + 1
        move_right = list(robot_pos)
        move_right[0] = move_right[0] + 1
        move_left = list(robot_pos)
        move_left[0] = move_left[0] - 1
        print("-------------------------------------------------------")
        log.write("\n-------------------------------------------------------\n")
        if(move_up[1] >= 1 and move_up != robot_old_pos):
            if(is_valid_pos(grid, move_up)):
                new_state = recod_state(grid, move_up, goal_pos, "U")
                history.append(new_state)

        if(move_down[1] <= len(grid)):
            if(is_valid_pos(grid, move_down)):
                new_state = recod_state(grid, move_down, goal_pos, "D")
                history.append(new_state)

        if(move_right[0] <= len(grid[0])):
            if(is_valid_pos(grid, move_right)):
                new_state = recod_state(grid, move_right, goal_pos, "R")
                history.append(new_state)

        if(move_left[0] >= 1):
            if(is_valid_pos(grid, move_left)):
                new_state = recod_state(grid, move_left, goal_pos, "L")
                history.append(new_state)

        sort_history(history)
        robot_old_pos = list(robot_pos)
        robot_pos = history[0]["pos"]
        grid[robot_old_pos[1] - 1][robot_old_pos[0] -
                                   1] = grid[robot_old_pos[1] - 1][robot_old_pos[0] - 1].replace("& ", "- ")
        board[robot_old_pos[1] - 1][robot_old_pos[0] -
                                    1] = "1"
        grid[robot_pos[1] - 1][robot_pos[0] - 1] = "& " + \
            grid[robot_pos[1] - 1][robot_pos[0] - 1]
        print('\nhistory:')
        log.write('\nhistory:\n')
        if(number_move == 0):
            print(history[0]['state'], '->', history[0]['h'])
        number_move += 1

        if(history[0]["h"] == 0):
            condiation = False
        for x in history:
            print(x["state"].replace("- ", ""), "->", x["h"], end=", ")
            log.write(x["state"].replace("- ", "") +
                      " -> " + str(x["h"]) + ", ")

        print()
        log.write("\n")
        print("-------------------------------------------------------")
        log.write("-------------------------------------------------------\n")

    print("number of steps:", number_move)
    log.write("number of steps: " + str(number_move)+"\n")
    for row in grid:
        print("| ", end="")
        log.write("| ")
        for col in row:
            print(col,  end=" | ")
            log.write(col+" | ")
        print()
        log.write('\n')
    print()
    log.write("\n")
    for row in board:
        log.write("| ")
        for col in row:
            print(col,  end=" | ")
            log.write(col+" | ")
        print()
        log.write('\n')
    print()


start_move()

log.close()
