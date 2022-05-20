import math
log = open('nn.log.txt', 'w', encoding="utf-8")

round_to = 5


def print_(t, m):
    log.write("\n"+str(t)+':\n')
    print(t+':')
    for i in m:
        print("\t", i)
        log.write("\t" + str(i)+"\n")
    pass
    log.write('\n')


def add_victor(v1, v2):
    v = []
    for i in range(len(v1)):
        v.append(round(v1[i] + v2[i], round_to),)
    return v


def scalr_victor(v, s):

    _v = list(v)
    for i in range(len(_v)):
        _v[i] *= s
        _v[i] = round(_v[i], round_to)
    return _v


def multi_victor(v1, v2):
    _v = []
    for i in range(len(v1)):
        _v.append(v1[i] * v2[i])
    return _v


def multi_matrix(m, v):
    _v = []
    sum = 0
    for i in range(len(m)):
        sum = 0
        for j in range(len(m[i])):

            sum += round(m[i][j] * v[j], round_to)
        _v.append(sum)
    return _v


def calc_actual_active_t(v, t):
    _v = []
    for i in range(len(v)):
        if v[i] >= t:
            _v.append(1)
        else:
            _v.append(0)
    return _v


def calc_actual_active_d(v):
    _v = []
    for i in range(len(v)):
        exp = math.exp(-v[i])
        _v.append(round(1 / (1 + exp), round_to))
    return _v


def calc_error_1(d, y):
    e = []
    for i in range(len(d)):
        e.append((d[i] - y[i]))
    return e


def calc_error_2(d, y):
    e = []
    for i in range(len(d)):
        e.append(round((d[i] - y[i]) * y[i] * (1 - y[i]), round_to))
    return e


def delta_w(eta, e, x):
    delta = []

    for i in range(len(e)):
        delta.append(scalr_victor(x, e[i] * eta))
    return delta


def update_w(w, delt):

    for i in range(len(w)):
        w[i] = add_victor(w[i], delt[i])


def tranpos_matrix(m):
    return [[m[j][i] for j in range(
        len(m))] for i in range(len(m[0]))]


# input layer
x = [[0, 1, 1, 1, 0, 3]]
# wight hiden layer
wh = [
    [0.75, 0.78, 0.34, 0.60, 0.08, 1.00],
    [0.38, 0.93, 0.16, 0.25, 0.23, 0.08],
    [0.57, 0.13, 0.79, 0.65, 0.91, 0.44],
    [0.08, 0.57, 0.31, 0.69, 0.15, 0.11],
    [0.05, 0.47, 0.53, 0.75, 0.83, 0.96],
    [0.53, 0.01, 0.17, 0.45, 0.54, 0.00],
]
# wight out layer
wo = [
    [0.77, 0.40, 0.91, 0.14, 0.14, 0.51],
    [0.82, 0.26, 0.18, 0.87, 0.85, 0.40],
    [0.87, 0.80, 0.26, 0.58, 0.62, 0.08],
    [0.08, 0.43, 0.15, 0.55, 0.35, 0.24],
]
# desaird output
d = [[0.9, 0.5, 0.5, 0.3]]

# delta or prceptron rule
isDelta = True


def hiden_layer_d(x, wh, wo):
    net_h = []
    active_h = []
    error_h = []
    delta_h = []
    net_o = []
    active_o = []
    error_o = []
    sgma_error_o = []
    delta_o = []
    # wh . X
    for i in range(len(x)):
        # net h
        net_h.append(multi_matrix(m=wh, v=x[i]))
        # activation yh
        if isDelta:
            active_h.append(calc_actual_active_d(net_h[i]))
        else:
            active_h.append(calc_actual_active_t(net_h[i], 0.1))
        # wo . yh
        for u in range(len(active_h)):
            # net o
            net_o.append(multi_matrix(m=wo, v=active_h[u]))
            # activation o
            if isDelta:
                active_o.append(calc_actual_active_d(net_o[u]))
            else:
                active_o.append(calc_actual_active_t(net_o[u], 0.1))
            # error outlayer
            error_o.append(calc_error_2(d[u], active_o[u]))
        # delta wo
        for u in range(len(active_h)):
            for j in range(len(active_h[u])):
                delta_o.append(delta_w(0.9, error_o[u], active_h[u]))
            # update wo
            update_w(wo, delta_o[i])

        # sum error
        for u in range(len(error_o)):
            for j in range(len(error_o[u])):
                sgma_error_o.append(scalr_victor(wo[j], error_o[u][j]))

        sgma_error_o = [[sgma_error_o[j][i] for j in range(
            len(sgma_error_o))] for i in range(len(sgma_error_o[0]))]
        for u in range(len(sgma_error_o)):
            sum = 0
            for j in range(len(sgma_error_o[u])):
                sum += sgma_error_o[u][j]
            sgma_error_o[u] = sum
        # error hiden layer
        for u in range(len(active_h)):
            error_h.append([])
            for j in range(len(active_h[i])):
                y = active_h[u][j]
                error_h[u].append(
                    round((y * (1 - y) * sgma_error_o[j]), round_to))
        # delta wh
        delta_h.append(delta_w(0.9, error_h[i], x[i]))
        # update wh
        update_w(wh, delta_h[i])
        print_('x', x[i])
        print_('wo', wo)
        print_('wh', wh)
        print_('net h', net_h)
        print_('active h', active_h)
        print_('net_o', net_o)
        print_('active_o', active_o)
        print_('error_o', error_o)
        print_('error_h', error_h)
        print_('delta_o', tranpos_matrix(delta_o[i]))
        print_('delta_h', tranpos_matrix(delta_h[i]))
        print_('updated wo', wo)
        print_('updated wh', wh)
        log.write('\n'+"---------- "+str(i)+" ----------"+"\n")


hiden_layer_d(x, wh, wo)
