firstOne = [[0] * 3] * 2
secondOne = [[1] * 2 for _ in range(3)]
firstOne[1][1]
print(secondOne)

# 3

secondOne[2][1] = 3
print(secondOne)

#4

mergedOne = firstOne + secondOne
print(mergedOne)

#5

print(mergedOne[:2][:2])

#6

mergedOne.append(4)
mergedOne.append(5)
print(mergedOne)

#7

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def intersection(a,b):
    return list(set(a) & set(b))
print("Common numbers list is:")
print(intersection(a,b))

#8

liss = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
def unic_num(x):
    set_list = set (x)
    unic_list = list (set_list)
    print("The unic numbers list is:")
    print(unic_list)
unic_num(liss)
