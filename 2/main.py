#aoc 2021 #2
#part1
'''
hor_pos = 0
depth = 0

lst = open("venv/input", "r").readlines()
for i in lst:
    x = i.split()
    if(x[0] == "forward"):
        hor_pos += int(x[1])
    elif (x[0] == "down"):
        depth += int(x[1])
    elif (x[0] == "up"):
        depth -= int(x[1])

print(hor_pos*depth)
'''

#part2
hor_pos = 0
depth = 0
aim = 0

lst = open("venv/input", "r").readlines()

for i in lst:
    x = i.split()
    if(x[0] == "forward"):
        hor_pos += int(x[1])
        depth += aim * int(x[1])
    elif (x[0] == "down"):
        aim += int(x[1])
    elif (x[0] == "up"):
        aim -= int(x[1])

print(hor_pos*depth)
