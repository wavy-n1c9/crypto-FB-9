import re
import math

def entrop_let(str_txt, filename, letters):
    lettersq=len(letters)
    entr=0
    let_q = [None] * lettersq
    let_freq_mass = [None] * lettersq
    len_txt = len(str_txt)
    for i in range(0, lettersq):
        let_freq_mass[i] = (str_txt.count(letters[i])) / len_txt
    # entrop:
    for i in range(0, lettersq):
        if(let_freq_mass[i]!=0):
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

    filename.write("\n" + "Sorted dict(letter+freq):\n")
    filename.write(str(sorted_dict))
    filename.write("\nEntrop: " + str(entr))


def entrop_bigr1(lett, textbigr,filename):
    lentxt=len(textbigr)
    alph_l=len(lett)
    mass_bigr = [[lett[k] + lett[i] for i in range(alph_l)] for k in range(alph_l)]
    values=[[None]*lentxt]*lentxt
    for i in range(alph_l):
        for j in range(alph_l):
            freq=(textbigr.count(mass_bigr[i][j]) / lentxt)
            values[i][j] = freq
            mass_bigr[i][j]= mass_bigr[i][j]+(" is ")+str(freq)
    for i in range(alph_l):
        for j in range(alph_l):
<<<<<<< Updated upstream
            filename.write(mass_bigr[i][j]+" ")
=======
            filename.write(" " + mass_bigr[i][j]+" -> "+str(values[i][j])+" ")
>>>>>>> Stashed changes
        filename.write("\n")
    #Пошук ентропії
    entr=0
    for i in range(alph_l):
        for j in range(alph_l):
            if (values[i][j] != 0):
                entr = entr + (-(values[i][j]) * (math.log2(values[i][j])))
    filename.write("Entropy is: " + str(entr))



alpha = "абвгдежзийклмнопрстуфхцчшщыьэюя"
alpha2 = "абвгдежзийклмнопрстуфхцчшщыьэюя "
filesp = open('spaces.txt', 'r', encoding='utf-8') #filesp - file with spaces
filensp = open('nospaces.txt', 'r', encoding='utf-8') #without spaces
file2 = open('after.txt', 'w', encoding='utf-8') #result

text_str_nsp = filensp.read()
file2.write("Letters, no spaces: ")
file2.write("entrop for letters, no spaces")
entrop_let(text_str_nsp, file2, alpha)


# Розбиття тексту на біграми

txtbigramcross = [text_str_nsp[i:i+2] for i in range(len(text_str_nsp))] #перехресна
txtbigramnocross = [text_str_nsp[i:i+2] for i in range(0, len(text_str_nsp), 2)] # не перехресна
file2.write("\nBigram cross, no spaces \n")
entrop_bigr1(alpha, txtbigramcross, file2)
file2.write("\nBigram for no cross, no spaces \n")
entrop_bigr1(alpha, txtbigramnocross, file2)


#Робимо теж саме, але з пробілами

text_sp = filesp.read()

file2.write("\nEntrop for letters, with spaces\n")
entrop_let(text_sp, file2, alpha2)

txtbigramcross = [text_sp[i:i+2] for i in range(len(text_sp))] #перехресна
txtbigramnocross = [text_sp[i:i+2] for i in range(0, len(text_sp), 2)] # не перехресна

file2.write("\nBigram cross, with spaces \n")
entrop_bigr1(alpha2, txtbigramcross, file2)
file2.write("\nBigram for no cross, with spaces \n")
entrop_bigr1(alpha2, txtbigramnocross, file2)

file2.close()
filesp.close()
filensp.close()