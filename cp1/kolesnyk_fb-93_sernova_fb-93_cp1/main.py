import re
import math


def filter_str(str_txt):
    str_txt = re.sub("[^А-Яа-я]", "", str_txt)
    str_txt = str_txt.lower()
    return str_txt


def entrop_let(str_txt, filename):
    entr=0
    letters = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    let_q = [None] * 32
    let_freq_mass = [None] * 32
    len_txt = len(str_txt)
    for i in range(0, 32):
        let_freq_mass[i] = (str_txt.count(letters[i])) / len_txt
    # entrop:
    for i in range(0, 32):
        entr = entr + let_freq_mass[i] * math.log2(let_freq_mass[i])
    entr=-entr

    freq_dict = dict(zip(letters, let_freq_mass))
    sorted_values = sorted(freq_dict.values(), reverse=True)  # Sort the values
    sorted_dict = {}
    for i in sorted_values:
        for k in freq_dict.keys():
            if freq_dict[k] == i:
                sorted_dict[k] = freq_dict[k]
                break

    filename.write("\n" + "Sorted dict(letter+freq):\n" + str(sorted_dict))
    filename.write("\nEntrop(for symb): " + str(entr))


def entrop():
    bigrams=[]


file1 = open('before.txt', 'r', encoding='utf-8')
text_str = file1.read()
text_str = filter_str(text_str)

file2 = open('after.txt', 'w', encoding='utf-8')
file2.write(text_str)
entrop_let(text_str, file2)


file2.close()
file1.close()