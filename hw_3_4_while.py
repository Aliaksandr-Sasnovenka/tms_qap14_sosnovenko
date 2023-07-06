# 1

product = 1
i = 1
N = 5
while i <= N:
    product *= i
    i += 1
print(product)


# 2

def relation_size(s1, s2):
    j = 0
    while s1 / s2 > 0.1:
        s1 **= 2
        s2 **= 3
        j += 1
    return j


print(relation_size(1, 4))


# 3

def digits_(n):
    c = 0
    s = 0
    dig = 1
    while dig != 0:
        dig = n // (10 ** c)
        surplus = dig % 10
        c += 1
        s += surplus
    return c, s + dig


print(digits_(23))


# 4

def divAges(n1, n2):
    delta = 0
    if n1 - n2 < 0:
        while n2 / n1 > 2:
            n2 += 1
            n1 += 1
            delta += 1
    else:
        while n1 / n2 > 2:
            n2 += 1
            n1 += 1
            delta += 1
    return delta


print(divAges(5, 43))
