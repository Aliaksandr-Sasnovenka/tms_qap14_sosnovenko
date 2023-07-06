# 1

def fora(beg, end):
    summ = 0
    for a in range(beg, end + 1):
        summ += a
    return summ


print(fora(1, 4))

# 2
A = 5
B = 6
print(fora(A, B - 1))

# 3

bunchOfNumb = [2, -1, 4, 21, -8, 11, 45, -1, 3, 22]
cntr = 0
summB = 0
prod = 1
for i in bunchOfNumb:
    if i < 0:
        cntr += 1
        summB += i
    else:
        prod *= i
print("result is:" + "\nколькасць: " + str(cntr) + "\nсума: " + str(summB) + "\nздабытак: " + str(prod))

# 4

dict_sw = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17
}
minValue = dict_sw.get("Казак Анна")


def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]


for i in dict_sw.values():
    if i < minValue:
        minValue = i

print("the best result: " + str(get_keys_from_value(dict_sw, minValue)) + " " + str(minValue))

#5

array_init = [1, 5, 2, 9, 2, 9, 1]
array_rem = array_init.copy()
for z in range(0, len(array_init)):
    for y in range(z+1, len(array_init)):
        if array_init[z] == array_init[y]:
            array_rem.remove(array_init[z])
            array_rem.remove(array_init[y])
print(array_rem)
