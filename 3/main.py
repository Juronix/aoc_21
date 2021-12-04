# advent of code 3
# part 1
'''
lst = open("venv/input", "r").readlines()

gamma_rate_array = [[0 for x in range(2)]for y in range(0,len(lst[0])-1)]

for i in lst:
    for j in range(0,len(i)-1):
        if i[j] == "0":
            gamma_rate_array[j][0] += 1
        if i[j] == "1":
            gamma_rate_array[j][1] += 1

gamma_rate = 0b0
epsilon_rate = 0b0

for k, v in enumerate(reversed(gamma_rate_array)):
    if v[0] < v[1]:
        gamma_rate += 0b1 * (2**k)
    else:
        epsilon_rate += 0b1 * (2**k)

power_consumption = gamma_rate * epsilon_rate

print("power consumption =", power_consumption)
'''
# part 2
lst = open("venv/input", "r").readlines()
lst_copy = lst[:]


def getCommonValue(position, commontype, li):
    counter = [0, 0]
    for value in li:
        if value is not False:
            if value[position] == "0":
                counter[0] += 1
            if value[position] == "1":
                counter[1] += 1

    if commontype == "most" and counter[1] >= counter[0]:
        return 1
    if commontype == "most" and counter[1] < counter[0]:
        return 0
    if commontype == "least" and counter[1] < counter[0]:
        return 1
    if commontype == "least" and counter[1] >= counter[0]:
        return 0


# oxigen
oxygen = int("0", 2)
for k, v in enumerate(range(0, len(lst[0]) - 1)):
    commonValue = getCommonValue(k, "most", lst)
    for k2, v2 in enumerate(lst):
        if v2 is not False and int(v2[k]) != commonValue:
            lst[k2] = False
    count = 0
    last_index = 0
    for k2, v2 in enumerate(lst):
        if v2 is not False:
            count += 1
            last_index = k2
    if count == 1:
        oxygen = int(lst[last_index], 2)
        break

# co2
co2 = int("0", 2)
for k, v in enumerate(range(0, len(lst_copy[0]) - 1)):
    commonValue = getCommonValue(k, "least", lst_copy)
    for k2, v2 in enumerate(lst_copy):
        if v2 is not False and int(v2[k]) != commonValue:
            lst_copy[k2] = False
    count = 0
    last_index = 0
    for k2, v2 in enumerate(lst_copy):
        if v2 is not False:
            count += 1
            last_index = k2
    if count == 1:
        co2 = int(lst_copy[last_index], 2)
        break

print("the live support rating is: ", oxygen * co2)