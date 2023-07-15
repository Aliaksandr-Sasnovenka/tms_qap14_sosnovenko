# 1 printing input by using lambda
import re

in_in = lambda a: "Hello, " + a
in_in(input("Enter your name:"))

# 2 -//- for list

in_in_list = lambda x: list(map(in_in, x))
in_in_list(["Al", "Mal", "Pal"])


# 3 generator's section


def gen_test(array):
    numbext = array.copy()
    for i in range(len(array)):
        if array[i] < 0:
            numbext[i] = array[i] * (-1)
    yield numbext


numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

print(next(gen_test(numbers)))


# 4 Len a string words

class TheTheWordException(Exception):
    """Raised when a sentence contain the 'the' word"""
    pass


Sent = "thequick brown fox jumps over the lazy dog"
lisst = list(map(len, Sent.split()))
try:
    if re.search(r'\bthe\b', Sent):
        raise TheTheWordException

except TheTheWordException:
    print("Exception: the 'the' was founded")
else:
    print(lisst)
