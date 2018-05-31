# for circular list -> creates an internal loop
#from itertools import cycle

def main():
    print('Welcome to python course')
    #tuple implemenantion
    alphabetCaps = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    alphabetLower = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    #list implemenantion
    #alphabet = 'A a B b C c D d E e F f G g H h I i J j K k L l M m N n O o P p Q q R r S s T t U u V v W w X x Y y Z z'.split()

    print('Give a message for encryption')
    temp = input()
    print('Give key for encryption')
    key = int(input())

    encryptionDecryptionDictCaps = generateDict(alphabetCaps,key)
    encryptionDecryptionDictLower = generateDict(alphabetLower,key)

    encDec = encryptionDecryptionDictCaps
    encDec.update(encryptionDecryptionDictLower)

    encList = encrypt(temp,encDec)
    print(encList)
    print("Ciphered text: {}".format("".join(str(x) for x in encList)))
    decList = decrypt(encList,encDec)
    print(decList)
    print("Deciphered text: {}".format("".join(str(x) for x in decList)))


def generateDict(alphabet,key):
    dict = {}
    list_len = len(alphabet)
    for letter in range(0,list_len):
        if(letter+key>= list_len):
            dict[alphabet[letter]] = alphabet[-(list_len-(letter+key))]
        else:
            dict[alphabet[letter]] = alphabet[letter+key]
    return dict

def encrypt(temp,encDec):
    list = []
    for letter in range(0,len(temp)):
        list.append(encDec[temp[letter]])
    return list

def decrypt(temp,encDec):
    list = []
    for letter in range(0,len(temp)):
        for key,value in encDec.items():
            if(value == temp[letter]):
                list.append(key)
    return list

if __name__ == "__main__":
    main()
