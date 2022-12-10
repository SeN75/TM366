

import math


X = {}
V = {}
P = {}

g_best = []

phi1 = 0
phi2 = 0

number_of_point = 0


def enter_value():

    number_of_point = eval(input("Enter number of point: "))
    for point in range(number_of_point):
        _x = []
        _v = []
        _p = []

        _x = (input("X" + str(point + 1)).split(","))
        _v = (input("V" + str(point + 1)).split(","))
        _p = (input("P" + str(point + 1)).split(","))

        X["X"+str(point+1)] = _x
        V["V"+str(point+1)] = _v
        P["P"+str(point+1)] = _p
    g_best = input('Enter number values of G best: ').split(',')
    phi1 = eval(input("phi1: "))
    phi2 = eval(input("phi2: "))

    print_log()


def update_gBest():
    pass


def update_x_v(n):
    for p in range(len(V["V"+str(n)])):
        X["X"+str(n)][p] = velocity_calculated(n, p)


def velocity_calculated(n, p):
    _v = V["V"+str(n)][p]
    _pi = P["P"+str(n)][p]
    _x = X["X"+str(n)][p]
    _pg = g_best[p]
    _v = _v + phi1 * (_pi - _x) + phi2 * (_pg - _x)
    return _v


def start():
    enter_value()
    for n in number_of_point:
        update_x_v(n)
        print("time", n)
        print_log()


def print_log():
    print("X: ", X)
    print("V: ", V)
    print("P: ", P)
    print("g_best: ", g_best)
    print("phi1: ", phi1)
    print("phi2: ", phi2)


def minimum():
    pass


start()