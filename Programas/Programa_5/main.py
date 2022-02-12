# Vigenere encrypt algoritm
def createTableVigenere():
    alphabet = [chr(_) for _ in range(65, 91, 1)]
    vigenereTable = []
    i = 0
    while True:
        j = i
        endRow = 0
        vigenereTable.append([])
        while True:
            endRow += 1
            vigenereTable[i].append(alphabet[j])
            j += 1
            if j >= 26:
                j = 0
            if endRow >= 26:
                break
        i += 1
        if i >= 26:
            break
    return vigenereTable

def printTable(vigenereTable):
    for i in range(len(vigenereTable)):
        for j in range(len(vigenereTable)):
            print(vigenereTable[i][j], end=' ')
        print()

def getStrings():
    string_txt = ''
    string_key = ''
    while True:
        # get string text 
        string_txt = input('INSERT STRING: ')
        print(len(string_txt))
        # get key string 
        string_key =  input('INSERT KEY: ')
        print(len(string_key))
        # compare len of strings
        if len(string_txt) > len(string_key):
            break
    return string_txt, string_key

def getStringKey(string_txt, string_key):
    string_key_OUT = ''
    string_key_list = list(string_key)
    j = 0
    for i in string_txt:
        if i != ' ':
            if j >= len(string_key):
                j = 0
            string_key_OUT += str(string_key_list[j])
            j += 1
        else:
            string_key_OUT += ' '
    return string_txt, string_key_OUT

def encrypt(stringTxt, stringTxtKey):
    vigenereTable = createTableVigenere()
    stringEncrypt = []
    stringTxt = list(stringTxt)
    stringTxtKey = list(stringTxtKey)
    print('STRING :',stringTxt)
    print('TXT_KEY:',stringTxtKey)
    for c in range(len(stringTxt)):
        if stringTxt[c] == ' ':
            stringEncrypt.append(' ')
            continue
        for i in range(len(vigenereTable)):
            if stringTxt[c] == vigenereTable[0][i]:
                #print(vigenereTable[0][i])
                for j in range(len(vigenereTable)):
                    if stringTxtKey[c] == vigenereTable[j][0]:
                        #stringEncrypt += vigenereTable[i][j]
                        stringEncrypt.append(vigenereTable[i][j])
    return stringEncrypt

def decrypt(stringEncrypted, stringKey):
    vigenereTable = createTableVigenere()
    stringDecrypt = []
    encrypt, key = getStringKey(stringEncrypted, stringKey)
    stringTxtEnc = list(encrypt)
    stringTxtKey = list(key)
    print('STRING :',stringTxtEnc)
    print('TXT_KEY:',stringTxtKey)
    for c in range(len(stringTxtEnc)):
        if stringTxtEnc[c] == ' ':
            stringDecrypt.append(' ')
            continue
        for i in range(len(vigenereTable)):
            if stringTxtKey[c] == vigenereTable[0][i]:
                for j in range(len(vigenereTable)):
                    if stringTxtEnc[c] == vigenereTable[j][i]:
                        stringDecrypt.append(vigenereTable[0][j])
    return stringDecrypt


if __name__ == '__main__':
    print('\tSTART')
    while True:
        option = int(input(' ENCRYPT (1) \n DECRYTP (2) \n EXIT (3): '))
        if option == 1:
            stringIn, stringKey = getStrings()
            stringTxt, stringTxtKey = getStringKey(stringIn, stringKey)
            stringEncrypt = encrypt(stringTxt.upper(), stringTxtKey.upper())
            print('ENCRYPT:', stringEncrypt, '\n')
            #printTable(createTableVigenere())
        elif option == 2:
            stringIn, stringKey = getStrings()
            stringDecrypt = decrypt(stringIn.upper(), stringKey.upper())
            print('DECRYPT:', stringDecrypt, '\n')
        elif option == 3:
            print('\tEND')
            break
        else:
            print('ERROR... SELECT (1) or (2) or (3): ')
