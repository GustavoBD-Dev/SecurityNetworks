alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
    'w', 'x', 'y', 'z']

def encrypt(jumps, stringIn):
    stringOut = ''
    for i in stringIn:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                if (j+jumps) >= len(alphabet):
                    j -= len(alphabet)
                stringOut += alphabet[j+jumps]
    return stringOut

def decrypt(jumps, stringIn):
    stringOut = ''
    for i in stringIn:
        for j in range(len(alphabet)):
            if i == alphabet[j]:
                if (j+jumps) < 0:
                    j += len(alphabet)
                stringOut += alphabet[j-jumps]
    return stringOut

def getParams():
    jumps = 0
    stringIn = ''
    while True:
        jumps = int(input("INSERT NUMBER JUMPS: "))
        stringIn = input("INSERT STRING: ")
        if jumps > 0 and len(stringIn) > 0 and stringIn.isalpha():
            break
    return jumps, stringIn

while True:
    print('\nENCRYPT CESAR')
    option = int(input(' ENCRYPT (1) \n DECRYPT(2) \n EXIT(3) \n INSERT OPTION: \t'))
    if option == 1:
        print('\tENCRYPT')
        jumps, stringIn =  getParams()
        print('{} with {} jumps -> {}'.format(stringIn, jumps, encrypt(jumps, stringIn)))
    elif option ==2:
        print('\tDECRYPT')
        jumps, stringIn =  getParams()
        print('{} with {} jumps -> {}'.format(stringIn, jumps, decrypt(jumps, stringIn)))   
    elif option == 3:
        print('END PROGRAM')
        break
    else:
        print('INSERT OPTION VALID:::')
