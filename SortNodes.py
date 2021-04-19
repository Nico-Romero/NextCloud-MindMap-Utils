import sys
import json

def listChildren(children):
    for i in range(len(children)):
        print(str(i) + ': ' + children[i]['data']['text'])

def getNextChild(max):
    next = -1
    while not(next > -1 and next < max):
        input_var = input('Choose the next children of this node')
        try:
            next = int(input_var)
        except ValueError:
            print('Invalid input')
    return next

def reorder(km_node):
    node_tree = km_node.copy()

    if (len(km_node['children']) > 0):
        node_tree['children'] = []

        nodes = km_node['children']
        print(km_node['data']['text'])
        print('Sort the node children:')
        while len(nodes) > 1:
            listChildren(nodes)
            next = getNextChild(len(nodes))
            node_tree['children'].append(reorder(nodes[next]))
            del nodes[next]
        node_tree['children'].append(reorder(nodes[0]))

    return node_tree


if len(sys.argv) < 2:
    raise ValueError('Reorders nodes from a km file. Usage: SortNodes.py mindmap.km ordered.km')

km_map_file = sys.argv[1]

result_file = 'output.json'
if len(sys.argv) == 3:
    result_file = sys.argv[2]


with open(km_map_file, "r") as read_file:
    data = json.load(read_file)

mind_map = data["root"]

node_tree = reorder(mind_map)

with open(result_file, 'w') as outfile:
    json.dump(node_tree, outfile)
