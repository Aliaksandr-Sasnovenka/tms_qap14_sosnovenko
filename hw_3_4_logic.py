import re

var1 = 8
var2 = 7

#2

print((var1 % var2) and (var1 - var2) and (var1 != var2))
print(not(ord("A") % 13) and not(abs(ord("a") - ord("n")) % 13) and bool(var1 % var2))
print(~(ord("A") % 13) and ~(abs(ord("a") - ord("n")) % 13) and not(var1 % var2))
print((var1 % var2) and (var1 - var2) and (var1 == var2))

#3

print("'or' statement:")
print(bool("Me") or bool("You") or bool("-") or bool("doesn't") or bool("matter") or ',' or bool("never"))
print("You" and bool("I") or "are" or bool("being") or "Forever")
print("You" and bool(not"I") or not"are" or bool(not"being") or not"Forever")
print(bool(not"You") or bool("") or bool(not"-") or bool(not"doesn't") or bool(not"matter") or bool(not"never"))

#4
print("\nsection 4\n")
print(bool({           }))
