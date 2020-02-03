#!/usr/bin/env python3

import time,json,re

location = {'x':0, 'y':0}
paths = {}
positions = []
variable = 1
currentpath = 1

with open("input", 'r') as f:
    path = f.readlines()
    for item in path:
        item = re.sub("\\n", "", item)
        paths[variable] = item
        variable = variable + 1

totalpaths = len(paths.keys())

while currentpath <= totalpaths:
    trail = paths[currentpath].split(',')
    print(trail)
    for direction in trail:
        if direction.startswith('R'):
            for value in range(0,int(direction[1:])):
                change = int(location['x']) + 1
                location['x'] = change
                upload = str(location['x']) + ':' + str(location['y'])
                if upload not in positions:
                    positions.append(upload)
        if direction.startswith('L'):
            for value in range(0,int(direction[1:])):
                change = int(location['x']) - 1
                location['x'] = change
                upload = str(location['x']) + ':' + str(location['y'])
                if upload not in positions:
                    positions.append(upload)
        if direction.startswith('U'):
            for value in range(0,int(direction[1:])):
                change = int(location['y']) + 1
                location['y'] = change
                upload = str(location['x']) + ':' + str(location['y'])
                if upload not in positions:
                    positions.append(upload)
        if direction.startswith('D'):
            for value in range(0,int(direction[1:])):
                change = int(location['y']) - 1
                location['y'] = change
                upload = str(location['x']) + ':' + str(location['y'])
                if upload not in positions:
                    positions.append(upload)
    location = {'x':0, 'y':0}
    print(positions)
    paths[currentpath + totalpaths] = positions
    posistions = []
    currentpath = currentpath + 1

print(paths.keys())

# for position in paths[3]:
#     if position in paths[4]:
#         print(position)

# print(paths)
