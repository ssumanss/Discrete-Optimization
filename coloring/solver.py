#!/usr/bin/python
# -*- coding: utf-8 -*-


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))

    # build a trivial solution
    # color =        # set all possible color to each node
    solution = []
    dic = {k:list(range(0, edge_count))  for k in range(node_count)} # start with each node having 4 color
    for node, colors in dic.items():           # iterating over each node
        if len(colors) > 1:                    # if first node has more possible colors                                
            c = colors[0] 
            dic[node] = c                      # set node to first color
            solution.append(c)
            # print(dic)
            for edge in edges[:]:
                if node in edge:
                    other_node = None
                    if node == edge[0]:
                        other_node = edge[1]
                    else:
                        other_node = edge[0]

                    edges.remove(edge)

                    # print(edges)
                    # print(other_node)        # printing other node
                    if node < other_node and dic[node] in dic[other_node]:
                        # print(dic[other_node], colors[0])
                        dic[other_node].remove(colors[0])

                    # print(dic)
                
            # edges = edges
            
        # print(key, val)
    # print(node_count, edge_count)    
    # print(edges)
    # print(dic)                     # solution stored in dictionary
    # print(solution)
    # every node has its own color
    # solution = range(0, node_count)

    # prepare the solution in the specified output format
    output_data = str(max(solution)+1) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')

