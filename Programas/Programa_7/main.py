
# This funciton split each four letter the string, return list
def stringSplitEachFourChars(string):
    return [string[i:i+4] for i in range(0, len(string), 4)]

# This funciton swap the letters in string to 4 letters
def changePosition(string):
    ans = list(string)          # convert to list the string
    # swap the values
    ans[0], ans[1], ans[2], ans[3] = ans[1], ans[3], ans[2], ans[0]
    return ''.join(ans)         # return the list as string

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

def feistelEncrypt(string, nRounds):
    for i in range(nRounds):
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
        feistelEncrypt(stringSplit, 16)
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
        feistelEncrypt(stringSplit, 16)
