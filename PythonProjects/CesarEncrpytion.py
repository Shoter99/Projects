import sys

def encrypt(text,seed):
    text = text.lower()
    cypher = []
    for l in text:
        if l == " ":
            cypher.append(" ")
            continue
        ascii_num = ord(l)+seed
        if ascii_num > 122:
            ascii_num -= 26
        cypher.append(chr(ascii_num))
    return "".join(cypher)
        
def decrypt(text,seed):
    text = text.lower()
    cypher = []
    for l in text:
        if l == " ":
            cypher.append(" ")
            continue
        ascii_num = ord(l)-seed
        if ascii_num < 97:
            ascii_num += 26
        cypher.append(chr(ascii_num))
    return "".join(cypher)


try:
    plainText = sys.argv[1]
except:
    print("Nie podano wyrazu/szyfru")
    quit()
try:
    seed = sys.argv[2]
    seed = int(seed)
except:
    print("Nie podano argumentu 2")
    quit()
try:
    mode = sys.argv[3]
except:
    print('Nie podano trybu')
    quit()

if mode == 'en':
    print(encrypt(plainText, int(seed)))
elif mode == 'de':
    print(decrypt(plainText, int(seed)))
else:
    print('Podano zły tryb <en/de>')
