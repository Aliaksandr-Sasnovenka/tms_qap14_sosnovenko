#1

school = {
    "1a": 32,
    "2e": 29,
    "7b": 30,
    "7t": 22,
    "9i": 20,
    "8e": 32,
    "4a": 23,
    "10c": 21,
    "11c": 22,
    "1b": 27
}

#2

print(school.get("1a"))

#3

school["1a"] = 33
school["9i"] = 19
school["7t"] = 29

school.update({"1m": 20})
school.update({"1l": 11})

school.pop("7t")

print(school)
