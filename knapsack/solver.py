#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    print(input_data)

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))


    print(items)
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full



    # prepare the table
    dp_table = [ [ 0 for x in range(capacity + 1) ] for y in range (item_count + 1)]

    for item in items:
        col = item.index + 1
        wt = item.weight
        for x in range(1, capacity + 1):
            if x >= wt:
                dp_table[col][x] = max(dp_table[col - 1][x], item.value + dp_table[col - 1][x - wt])
                
            else:
                dp_table[col][x] = dp_table[col - 1][x]


            
    print("dptable")
    for row in dp_table:
        print(' '.join(map(str,row)))



    # preparing solution
    value = dp_table[-1][-1]
    weight = 0
    
    taken = []
    row = capacity
    item_rev = sorted(items, key=lambda x: x.index, reverse = True)
    # print(item_rev)
    for item in item_rev:
        print(row, item.index, dp_table[item.index + 1][row])
        if dp_table[item.index + 1][row] == dp_table[item.index][row] or dp_table[item.index + 1][row] == 0:
            print(row, item.index)
            taken.append(0)
        

        else:
            taken.append(1)
            row = row - item.weight

        
    taken.reverse()
    print(taken)

    obj = 0
    for item in items:
        obj += item.value * taken[item.index]

    if abs(obj - value) < 0.1:
        print("program is working fine")

    else:
        print("somthing is wrong, ", obj)    


    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

