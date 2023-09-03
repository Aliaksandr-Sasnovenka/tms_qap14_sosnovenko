# open the file
import os.path
import pickle

'''fileout_1 = open("hw6/numberlist.txt", "r")

# 1

word_list_1 = fileout_1.read().split()
if len(word_list_1) < 3:
    raise Exception("Alas, you sent less then 3 numbers")
print(word_list_1[0], word_list_1[1], word_list_1[-1])
fileout_1.close()

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
fileout_2.close()
'''


# 3. squares of floats
def sqrff(filepath):
    string_store = ''

    "Open the file"
    with open(filepath, "r+") as fileout_3:
        real_numb = fileout_3.read().split(' ')
        for y in real_numb:
            string_store += str(eval(y) ** 2) + ' '
        # truncate older data
        fileout_3.seek(0)
        fileout_3.write(string_store)
        fileout_3.truncate()


# 4. replaceable binary files
def replace_content(str1, str2):
    file11 = open("C:/Users/Alex/PycharmProjects/tms_qap14_sosnovenko/hw6/bin1.bin", 'wb')
    file12 = open("C:/Users/Alex/PycharmProjects/tms_qap14_sosnovenko/hw6/bin2.bin", 'wb')

    pickle.dump(str1, file11)
    pickle.dump(str2, file12)

    file11.close()
    file12.close()

    """read two above files"""
    file1 = open("C:/Users/Alex/PycharmProjects/tms_qap14_sosnovenko/hw6/bin1.bin", 'r+b')
    file2 = open("C:/Users/Alex/PycharmProjects/tms_qap14_sosnovenko/hw6/bin2.bin", 'r+b')

    """cross writing section"""
    d1 = pickle.load(file1)
    d2 = pickle.load(file2)
    file1.seek(0)
    file2.seek(0)
    file2.truncate()
    file1.truncate()
    pickle.dump(d1, file2)
    pickle.dump(d2, file1)
    file2.close()
    file1.close()


'''
# third section's func
sqrff("hw6/reality.txt")
# forth section's func
'''
bin1 = ["moisture", 96, "pickle"]
bin2 = ("w", "ist", "S")
replace_content(bin1, bin2)
