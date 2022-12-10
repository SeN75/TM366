

from tkinter.tix import Tree


nodes = [
    {
        "state": "c1",
        "cost": 0,
        "historical": 370,
        "nodes": [
            {'state': "c4", "cost": 276},
            {'state': "c5", "cost": 230},
            {'state': "c6", "cost": 625},
        ],
        "visited": False,
    },
    {
        "state": "c2",
        "cost": 0,
        "historical": 153,
        "nodes": [
            {'state': "c3", "cost": 153},

        ],
        "visited": False,
    },
    {
        "state": "c3",
        "cost": 0,
        "historical": 0,
        "nodes": [
            {'state': "c2", "cost": 153},
            {'state': "c4", "cost": 228},
            {'state': "c5", "cost": 301},
        ],
        "visited": False,
    },
    {
        "state": "c4",
        "cost": 0,
        "historical": 228,
        "nodes": [
            {'state': "c1", "cost": 276},
            {'state': "c3", "cost": 228},
            {'state': "c5", "cost": 365},
        ],
        "visited": False,
    },
    {
        "state": "c5",
        "cost": 0,
        "historical": 301,
        "nodes": [
            {'state': "c1", "cost": 230},
            {'state': "c4", "cost": 365},
            {'state': "c6", "cost": 510},
        ],
        "visited": False,
    },
    {
        "state": "c6",
        "cost": 0,
        "historical": 256,
        "nodes": [
            {'state': "c1", "cost": 625},
            {'state': "c5", "cost": 510},
        ],
        "visited": False,
    },
]


def get_node(state):
    for i in range(len(nodes)):
        if (nodes[i]['state'] == state):
            return nodes[i]
    return nodes[0]


def search_shorter(node):
    for i in range(2):
        n = node
        child = n['nodes']

        # print(child)
        for i in range(len(child)):
            g = get_node(child[i]['state'])
            if g['visited'] == False:
                child[i]['f'] = child[i]['cost'] + g['historical']
                child[i]['visited'] = False
                print(child[i]['cost'], "+",
                      g['historical'], "=", child[i]['f'])
            else:
                child[i]['visited'] = True

        node['visited'] = True
        sort_child(child)

        n = node
        for x in n:
            if not x == 'nodes':
                print(x, ":", n[x])
            else:
                print(x, ":")
                for j in n[x]:
                    print('\t', j)
        # print(node)


def sort_child(child):
    for i in range(len(child)):
        min_idx = i
        for j in range(i+1, len(child)):
            if ("f" in child[j] and 'f' in child[min_idx]
                    and child[min_idx]["f"] > child[j]["f"]):
                min_idx = j
        child[i], child[min_idx] = child[min_idx], child[i]


search_shorter(nodes[0])

# for x in nodes[0]:
#     print(x, ":", nodes[0][x])
