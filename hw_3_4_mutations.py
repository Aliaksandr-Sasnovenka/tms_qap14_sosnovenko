# 1

robinBobbin = "Robin Singh"
fmml = "I love arrays they are my favorite"
print(robinBobbin.rsplit())
print(fmml.rsplit())

# 2

name = ['Ivan', 'Ivanou']
txt = "Привет, {} {}! Добро пожаловать в {} {}".format(name[0], name[1], "Minsk", "Belarus")
print(txt)

# 3

arrayTemp = ["I", "love", "arrays", "they", "are", "my", "favorite"]
arrayStr = ""
for i in arrayTemp:
    arrayStr += i + " "
print(arrayStr)

# 4
print("list insertion")
listBar = ["first", "second", "third", "forth", "fifth", "sixth",
           "seventh", "eighth", "ninth", "last"]
listBar.insert(2, "item")
print(listBar)

# 5

a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}


def mergeDictionary(var1, var2):
    c = {**a, **b}
    for key, x in c.items():
        if key in a and not key in b:
            c[key] = [a[key], None]
        elif not key in a and key in b:
            c[key] = [None, x]
        else:
            c[key] = [a[key], x]
    return c


ab = mergeDictionary(a, b)
print(ab)
