alphabet = {
    'A' : '00000', 'B' : '00001', 'C' : '00010', 'D' : '00011',
    'E' : '00100', 'F' : '00101', 'G' : '00110', 'H' : '00111',
    'I' : '01000', 'J' : '01001', 'K' : '01010', 'L' : '01011',
    'M' : '01100', 'N' : '01101', 'O' : '01110', 'P' : '01111',
    'Q' : '10000', 'R' : '10001', 'S' : '10010', 'T' : '10011',
    'U' : '10100', 'V' : '10101', 'W' : '10110', 'X' : '10111',
    'Y' : '11000', 'Z' : '11001', '0' : '11010', '1' : '11011',
    '2' : '11100', '3' : '11101', '4' : '11110', '5' : '11111'
}

def stringToBinary(string):
    stringBin = ''
    for char in string:
        for key,value in alphabet.items():
            if char.upper() == key:
                stringBin += value
    return stringBin

def binaryToString(stringBin):
    # split values of stringBin each 5 chars
    stringBinSplit = [stringBin[i:i+5] for i in range(0, len(stringBin), 5)]
    string = '' # string to add char encryption
    for i in stringBinSplit: # iterate the string 
        for key,value in alphabet.items():
            if i == value: # if string binary is equal to value in alphabet 
                string += key # add char to string 
    return string

def XOR(string1, string2):
    stringXOR = ''
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            stringXOR += '0'
        else:
            stringXOR += '1'
    return stringXOR

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
    # concatenate string KEY with equal len TXT
    while len(string_key) < len(string_txt):
        string_key += string_key
    # we the extract the number of characters
    string_key = string_key[0 : len(string_txt)]
    return string_txt, string_key



if __name__ == '__main__':
    print('::::START PROGRAM::::')
    while True:
        option = int(input(' ENCRYPT (1) \n DECRYPT (2) \n EXIT (3): \n INSERT OPTION: '))
        if option == 1:
            # input and validate the strings
            string_txt, string_key = getStrings()
            print(string_txt)
            print(string_key)
            # Convert string to binary
            string_txt_bin = stringToBinary(string_txt)
            string_key_bin = stringToBinary(string_key)
            print(string_txt_bin)
            print(string_key_bin)
            # Operation XOR
            stringXOR = XOR(string_txt_bin, string_key_bin)
            print(stringXOR)
            # Converto string binary to Alphabet
            encryption = binaryToString(stringXOR)
            print(encryption)

        elif option == 2:
            # input and validate strings 
            string_txt, string_key = getStrings()
            print(string_txt)
            print(string_key)
            # Convert string to binary
            string_txt_bin = stringToBinary(string_txt)
            string_key_bin = stringToBinary(string_key)
            print(string_txt_bin)
            print(string_key_bin)
            # Operation XOR
            stringXOR = XOR(string_txt_bin, string_key_bin)
            print(stringXOR)
            # Converto string binary to Alphabet
            decryption = binaryToString(stringXOR)
            print(decryption)

        elif option == 3:
            print('END PROGRAM:::::')
            break
        else:
            print('INSERT VALID OPTION....')

