#розширений алгоритм евкліда
alphabet = "абвгдежзийклмнопрстуфхцчшщыьэюя" # "ё" "ъ" в нашем тексте нет
alen = len(alphabet)
f=open('07.txt', 'r', encoding='utf-8')
encoded_text = f.read()


#розширений алгоритм евкліда ax + by = gcd(a,b)     ret gcd, x, y
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

#пошук оберненого
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return False
    else:
        return x % m


def modulation(a, b, mod):  # ax=b modn
    a = a % mod
    b = b % mod
    d = egcd(a, mod)
    x = []
    if d==1 :
        x.append((modinv(a,mod)*b)%mod)
    else:
        #i dont know
        if b % d != 0:
            return -1
        else:
            a_rek = a / d
            b_rek = b / d
            n_rek = mod / d
            x_ret = modulation(a_rek, b_rek, n_rek)
            return int(x_ret)

def bigr_to_num(bigr,mod):
    num=alphabet.index(bigr[0])*mod+alphabet.index(bigr[1])
    return num

def num_to_bigr(num, mod):
    bigr=alphabet[num//mod]+alphabet[num % mod]
    return bigr


#біграми з найвищою частотою
top_bigr_en=['лл', 'ул', 'еб', 'цл', 'ле']
top_bigr_plain = ['ст', 'но', 'ен', 'ни', 'от']

