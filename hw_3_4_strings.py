import math
import re
strong = "Addis Ababa"
firstChar = strong[0]
lastChar = strong[-1]
thirdChar = strong[2]
minusThirdChar = strong[-3]
lengthTemp = strong.__len__()

# core of the string

weak = "have a seat, please"
first8 = weak[:8]
meanT = weak.__len__()/2
print("core:")
for x in range(math.floor(meanT) - 2, math.floor(meanT) + 2):
    print(weak[x])

# every third element

everyThird = ''
print("everyThirdValue:")
for x in range(len(weak)):
    if x % 3 == 0:
        everyThird += weak[x]
print(everyThird)

# string negate

temporaryStr = ''
for x in range(len(weak)):
    temporaryStr = temporaryStr + weak[-x]
print(temporaryStr)

# my name

result = re.findall(r"\w+", 'my name is name')
i = 0
jee = 0
while i < 2:
    for j in range(len(result)):
        if result[j] == "name":
            i += 1
            jee += 1
result[jee + 1] = "Alexandr"
listToStr = ' '.join(map(str, result))
print(listToStr)
