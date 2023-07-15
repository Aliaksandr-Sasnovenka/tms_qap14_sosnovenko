import re


def cesarcode(txt: str, shift=3):
    mut_string = ''
    c = 0
    while c <= len(txt) - 1:
        if re.match(r"\w", txt[c]):
            mut_string = mut_string + str(chr(ord(txt[c]) + shift))
        else:
            print("Look at this positions:" + " " + str(c) + ' ' + txt[c])
            mut_string = mut_string + txt[c]
        c += 1
    return mut_string


def cesardecode(txt, shift=3):
    source_txt = ''
    c = 0
    while c <= len(txt) - 1:
        if re.match(r'\w', txt[c]):
            source_txt = source_txt + str(chr(ord(txt[c]) - shift))
        else:
            print("Look at this positions:" + " " + str(c) + ' ' + txt[c])
            source_txt = source_txt + txt[c]
        c += 1
    return source_txt


print(cesarcode("Куй пока горячо"))
print(cesardecode(cesarcode("be good with a soldering iron")))
