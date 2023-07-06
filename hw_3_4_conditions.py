# 1

x = input("givie me a number:")
x = int(x)
if x >= 0:
    x += 1
print("plus one if positive:" + str(x))


# 2

def numberOfPositives(a, b, c):
    counter = 0
    e = locals()
    for i in e:
        if int(e.get(i)) > 0:
            counter += 1
    return counter


var1 = 1
var2 = -2
var3 = 3
print("how many arguments are positive:")
print(numberOfPositives(var1, var2, var3))

# 3

print('\nleap year\n')


def leap_year(year):
    days = 0
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            days = 365
        else:
            days = 366
    else:
        days = 365
    return days


print(leap_year(1999))

#4

daysOfWeek = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
print(daysOfWeek.get(3))

#5

def mass_defect(numb, mass):
    malpa = {
        1: "1",
        2: "10**(-6)",
        3: "10**(-3)",
        4: "10**3",
        5: "10**2"
    }
    return mass*eval(malpa.get(numb))


print(mass_defect(3, 2200))
