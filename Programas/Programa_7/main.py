
# This funciton split each four letter the string, return list
def stringSplitEachFourChars(string):
    return [string[i:i+4] for i in range(0, len(string), 4)]

# This funciton swap the letters in string to 4 letters
def changePosition(string):
    ans = list(string)          # convert to list the string
    # swap the values
    ans[0], ans[1], ans[2], ans[3] = ans[1], ans[3], ans[2], ans[0]
    return ''.join(ans)         # return the list as string

def restartPosition(block):
    ans = list(block)
    ans[0], ans[1], ans[2], ans[3] = ans[3], ans[0], ans[2], ans[1]
    return ''.join(ans)

# This function increment the position letter
def incrementLetter(string):
    # add char with ascii value to array
    alphabet = [chr(_) for _ in range(65, 91, 1)]
    aux = []
    for i in range(len(string)):
        for j in range(len(alphabet)):
            if string[i] == alphabet[j]:
                if j+1 >= len(alphabet):
                    aux.append(alphabet[(j-len(alphabet))+1])
                else:
                    aux.append(alphabet[j+1])
    return ''.join(aux)

def decrementLetter(string):
    # add char with ascii value to array
    alphabet = [chr(_) for _ in range(65, 91, 1)]
    aux = []
    for i in range(len(string)):
        for j in range(len(alphabet)):
            if string[i] == alphabet[j]:
                if j-1 < 0:
                    aux.append(alphabet[(j+len(alphabet))-1])
                else:
                    aux.append(alphabet[j-1])
    return ''.join(aux)

def feistelEncrypt(string, nRounds):
    stringList = []
    for i in range(nRounds):
        print("\tROUND #{}".format(int(i)+1))
        stringList = []
        for i in range(len(string)):
            if i%2 == 1:
                ans = incrementLetter(string[i])
                stringList.append(ans)
            else:
                stringList.append(string[i])
        print(stringList)

        for i in range(len(stringList)):
            if i%2 == 1:
                ans = changePosition(stringList[i])
                stringList[i] = ans
        print(stringList)

        string = stringList
        stringList = []
        for i in range(len(string)):
            if i%2 != 1:
                ans = incrementLetter(string[i])
                stringList.append(ans)
            else:
                stringList.append(string[i])
        print(stringList)

        for i in range(len(stringList)):
            if i%2 != 1:
                ans = changePosition(stringList[i])
                stringList[i] = ans
        print(stringList)
        string = stringList
        print()
    return ''.join(stringList)

def feistelDecrypt(stringEncoded, nRounds):
    ans = []
    for i in range(int(nRounds)):
        print("\tROUND #{}".format(int(i)+1))
        ans = []
        for i in range(len(stringEncoded)):
            if i%2 != 1:
                ans.append(restartPosition(stringEncoded[i]))
            else:
                ans.append(stringEncoded[i])
        print(ans)
        
        aux = []
        for i in range(len(ans)):
            if i%2 != 1:
                aux.append(decrementLetter(ans[i]))
            else:
                aux.append(ans[i])
        print(aux)

        ans = []
        for i in range(len(aux)):
            if i%2 == 1:
                ans.append(restartPosition(aux[i]))
            else:
                ans.append(aux[i])
        print(ans)

        aux = []
        for i in range(len(ans)):
            if i%2 == 1:
                aux.append(decrementLetter(ans[i]))
            else:
                aux.append(ans[i])
        print(aux)

        stringEncoded = aux
        ans = aux
    return ''.join(aux)


if __name__ == "__main__":    
    string = "ELECTRICIDADYELECTRONICA"
    # add char with ascii value to array
    alphabet = [chr(_) for _ in range(65, 91, 1)]
    # print(alphabet)

    if len(string)%4 == 0:
        # split values of string each 4 chars
        stringSplit = stringSplitEachFourChars(string)
        print(stringSplit)
        print()
        ans = feistelEncrypt(stringSplit, 16)
        print("String encoded: " , ans)

        print("\nDECRYPT STRING -> {}".format(ans))
        stringSplit = stringSplitEachFourChars(ans)
        print(stringSplit)
        decoded = feistelDecrypt(stringSplit, 16)
        print("String decoded is: {}".format(decoded))
    else:
        i = 0
        # complete the string 
        while len(string)%4 != 0:
            string += alphabet[i]
            i += 1
        print(string)
        # split values of string each 4 chars
        stringSplit = stringSplitEachFourChars(string)
        print(stringSplit)
        print()
        ans = feistelEncrypt(stringSplit, 16)
        print("String encoded: " , ans)
        print("\nDECRYPT STRING -> {}".format(ans))
        stringSplit = stringSplitEachFourChars(ans)
        print(stringSplit)
        decoded = feistelDecrypt(stringSplit, 16)
        print("String decoded is: {}".format(decoded))