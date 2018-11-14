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


    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))


    def dp_solver(item_count, capacity, items):
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


        # preparing solution
        value = dp_table[-1][-1]
        status = 1
        
        taken = []
        row = capacity
        item_rev = sorted(items, key=lambda x: x.index, reverse = True)
        # print(item_rev)
        for item in item_rev:
            if dp_table[item.index + 1][row] == dp_table[item.index][row] or dp_table[item.index + 1][row] == 0:
                taken.append(0)
            

            else:
                taken.append(1)
                row = row - item.weight

            
        taken.reverse()   
        return (value, status, taken)


    value, status, taken = dp_solver(item_count, capacity, items)
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(status) + '\n'
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

