log = open('pso.log.txt', 'w', encoding="utf-8")
# TMA Q3
# swarm = [
#     {
#         "position": [-2, -1, -1],
#         'velocity': [0.5, 0.7, 1.7],
#         "bestPos": [0, 2, -2],
#         "bestFit": 0,
#         "posFit": 0
#     },
#     {
#         "position": [0, -2, 2],
#         'velocity': [-0.2, -2.1, -0.8],
#         "bestPos": [1, -1, 0],
#         "bestFit": 0,
#         "posFit": 0
#     },
#     {
#         "position": [-2, 1, 1],
#         'velocity': [1.4, -1.1, 1],
#         "bestPos":  [-1, 0, -1],
#         "bestFit": 0,
#         "posFit": 0
#     }
# ]

# gBest = {
#     "position": [0, 0, -2],
#     "posFit": 0
# }

swarm = [
    {
        "position": [-1, 0, 1],
        'velocity': [-0.1, -0.6, -0.4],
        "bestPos": [0, -2, 0],
        "bestFit": 0,
        "posFit": 0
    },
    {
        "position": [1, -1, 1],
        'velocity': [-1.3, -0.9, -1.4],
        "bestPos": [0, -2, 0],
        "bestFit": 0,
        "posFit": 0
    },
    {
        "position": [-1, 0, 1],
        'velocity': [-0.5, -1.1, -0.7],
        "bestPos":  [-2, 0, -2],
        "bestFit": 0,
        "posFit": 0
    }
]
gBest = {
    "position": [-1, -2, -1],
    "posFit": 0
}


def sub_victor(v1, v2):
    v = []
    for i in range(len(v1)):
        v.append(round(v1[i] - v2[i], 2))
    return v


def add_victor(v1, v2):
    v = []
    for i in range(len(v1)):
        v.append(round(v1[i] + v2[i], 2))
    return v


def scalr_victor(v, s):
    _v = list(v)
    for i in range(len(_v)):
        _v[i] *= s
        _v[i] = round(_v[i], 2)
    return _v


def calculate_velocity(s):
    v = s["velocity"]
    xi = s['position']
    pi = s['bestPos']
    pg = gBest['position']

    phi1 = 0.2
    # phi1 = 0.3
    pix = list(sub_victor(pi, xi))
    phi2 = 0.4
    # phi2 = 0.2
    pig = list(sub_victor(pg, xi))

    phi1_pi_x = list(scalr_victor(pix, phi1))
    phi2_pg_x = list(scalr_victor(pig, phi2))

    new_velocity = list(add_victor(v, phi1_pi_x))
    new_velocity = list(add_victor(new_velocity, phi2_pg_x))
    print("v = v + phi1 (pi - xi) + phi2 (pg - x)")
    print("v =", v, "+ ", phi1, "(", pi, "-", xi, ") +",
          phi2, "(", pg, "-", xi, ")")
    print("v = ", v, "+", phi1, "(", pix, ")", "+", phi2, '(', pig, ")")
    print("v = ", v, "+", phi1_pi_x, "+", phi2_pg_x)

    print("\nv = ", new_velocity)

    log.write("\nv = v + phi1 (pi - xi) + phi2 (pg - x)")
    log.write("\nv = " + str(v) + " + " + str(phi1) + " ( " + str(pi) + " - " + str(xi) + " ) +" +
              str(phi2) + " ( " + str(pg) + " - " + str(xi) + " )")
    log.write("\nv = " + str(v) + " + " + str(phi1) +
              " ( " + str(pix) + " ) " + " + " + str(phi2) + ' ( ' + str(pig) + " ) ")
    log.write("\nv = " + str(v) + " + " +
              str(phi1_pi_x) + " + " + str(phi2_pg_x))
    log.write("\nv = " + str(new_velocity) + "\n")
    return new_velocity


def fitness_calculater(v):
    # x1 = 7 * math.pow(v[0], 1)
    # x2 = 6 * math.pow(v[1], 4)
    # x3 = 4 * math.pow(v[2], 5)
    # return x1 + x2 + x3
    x1 = 5 * math.pow(v[0], 1)
    x2 = 10 * math.pow(v[1], 3)
    x3 = 1 * math.pow(v[2], 5)
    return x1 + x2 + x3


def new_pos(s):
    new_pos = []
    for i in range(len(s['velocity'])):
        new_pos.append(s['position'][i] + s['velocity'][i])
    return new_pos


for x in range(2):
    print("time:", x+1)
    for s in swarm:
        print()

        s['velocity'] = calculate_velocity(s)
        s['position'] = new_pos(s)

        s['posFit'] = (fitness_calculater(s['position']))

       

        print()
    for s in swarm:
        s['bestFit'] = fitness_calculater(s['bestPos'])
        gBest['posFit'] = fitness_calculater(gBest['position'])

        if s['posFit'] < s['bestFit']:
            s['bestFit'] = s['posFit']
            s['bestPos'] = s['position']

        if s['posFit'] < gBest['posFit']:
            gBest['posFit'] = s['posFit']
            gBest['position'] = s['position']
        log.write(
            "\n-------------------------------------------------------------------\n")
        for key in s:
            print(key, ":", s[key])
            log.write(str(key) + " : " + str(s[key])+'\n')
        print('gBest: ', gBest)
        log.write('\ngBest: ' + str(gBest)+", ")
        log.write(
            "\n-------------------------------------------------------------------\n")
