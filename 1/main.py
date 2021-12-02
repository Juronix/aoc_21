# advent of code 2021 #1
# part 1
"""
f = open("venv/input", "r")

inc_counter = 0
prev_int = 0

for x in f:
    if prev_int != 0:
        if prev_int < int(x):
            inc_counter += 1
    prev_int = int(x)

print(inc_counter)
f.close()
"""
#part2

lst = open("venv/input", "r").readlines()

inc_counter = 0
index = 0

for x in lst:
    if index > 2:
        if int(lst[index-3])+int(lst[index-2])+int(lst[index-1]) < int(lst[index-2])+int(lst[index-1])+int(x):
            inc_counter += 1
    index += 1

print(inc_counter)
