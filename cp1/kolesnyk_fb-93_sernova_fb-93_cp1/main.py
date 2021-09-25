file = open('before.txt', 'r')
textstr = file.read()
textstr.lower()
newstring = "".join(filter(str.isalpha, textstr))

