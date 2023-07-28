# open the file
import os.path

fileout_1 = open("hw6/numberlist.txt", "r")

# 1

word_list_1 = fileout_1.read().split()
if len(word_list_1) < 3:
    raise Exception("Alas, you sent less then 3 numbers")
print(word_list_1[0], word_list_1[1], word_list_1[-1])

# 2 evens and even odds

fileout_2 = open("hw6/intergers", "r")
word_list_2 = fileout_2.read().split()
if os.path.exists("hw6/even_integers.txt") or os.path.exists("hw6/odd_integers.txt"):
    open("hw6/even_integers.txt", "w")
    open("hw6/odd_integers.txt", "w")
for i in word_list_2:
    if int(i) % 2 == 0:
        open("hw6/even_integers.txt", "a").write(" " + i)
    else:
        open("hw6/odd_integers.txt", "a").write(" " + i)

# 3. squares of floats

string_store = ''
"Open the file"
with open("hw6/reality.txt", "r+") as fileout_3:
    real_numb = fileout_3.read().split(' ')
    for y in real_numb:
        string_store += str(eval(y)**2) + ' '
    # truncate older data
    fileout_3.seek(0)
    fileout_3.write(string_store)
    fileout_3.truncate()
fileout_3.close()

# 4. replaceable binary files

bin1 = ["moisture", 96, "pickle"]
bin2 = ("w", "ist", "S")
file1 = open("hw6/bin1.bin", 'wb')
file2 = open("hw6/bin2.bin", 'wb')

"""to take the pickle method"""
import pickle
pickle.dump(bin1, file1)
pickle.dump(bin2, file2)

"""read two above files"""
file1 = open("hw6/bin1.bin", 'rb+')
file2 = open("hw6/bin1.bin", 'rb+')

"""cross writing section"""
d1 = pickle.load(file1)
d2 = pickle.load(file2)
pickle.dump(d1, file2)
pickle.dump(d2, file1)
