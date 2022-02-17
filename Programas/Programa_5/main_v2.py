
# create the alphabet and save the char in the list
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = list(alphabet)

stringTxt = 'INGENIEROS CANSADOS'
stringKey = 'ICOS'

stringTxt = list(stringTxt)
stringKey = list(stringKey)

# INGENIEROS CANSADOS
# ICOSICOSIC COSICOSI
j = 0
stringOut = []
for i in stringTxt:         # iterate the string input
    if i != ' ':            # if char not is ' '
        if j  >= len(stringKey): # restart position
            j = 0                
        stringOut.append(stringKey[j]) # add the char in position
        j += 1              # increase the position in the list key
    else:
        stringOut.append(' ')          # add ' '

print(stringTxt)
print(stringOut)

x = []
y = []
for i in range(len(stringTxt)):
    if stringTxt[i] == ' ':
        x.append(' ')
    else:
        for j in range(len(alphabet)):
            if stringTxt[i] == alphabet[j]:
                x.append(j)
for i in range(len(stringOut)):
    if stringOut[i] == ' ':
        y.append(' ')
    else:
        for j in range(len(alphabet)):
            if stringOut[i] == alphabet[j]:
                y.append(j)

z = []
for i in range(len(x)):
    if i == ' ':
        z.append(' ')
        continue
    else:
        z.append(x[i]+y[i])

print(x)
print(y)
print(z)

"""abd = []
for i in range(len(z)):
    abd.append(alphabet[i])"""

for i in range(len(z)):
    if z[i] == '  ':
        print(' ', end=' ')
        continue
    else:
        if int(z[i]) > 26:
            print(alphabet[z[i]-26], end=' ')
        else:
            print(alphabet[z[i]], end=' ')




stringTxt = 'JGNASNMW A YKTOVIUJ'
stringKey = 'USA'

stringTxt = list(stringTxt)
stringKey = list(stringKey)

# INGENIEROS CANSADOS
# ICOSICOSIC COSICOSI
j = 0
stringOut = []
for i in stringTxt:         # iterate the string input
    if i != ' ':            # if char not is ' '
        if j  >= len(stringKey): # restart position
            j = 0                
        stringOut.append(stringKey[j]) # add the char in position
        j += 1              # increase the position in the list key
    else:
        stringOut.append(' ')          # add ' '

print(stringTxt)
print(stringOut)

x = []
y = []
for i in range(len(stringTxt)):
    if stringTxt[i] == ' ':
        x.append(' ')
    else:
        for j in range(len(alphabet)):
            if stringTxt[i] == alphabet[j]:
                x.append(j)
for i in range(len(stringOut)):
    if stringOut[i] == ' ':
        y.append(' ')
    else:
        for j in range(len(alphabet)):
            if stringOut[i] == alphabet[j]:
                y.append(j)

z = []
for i in range(len(x)):
    if x[i] == ' ':
        z.append(' ')
        continue
    else:
        z.append(int(x[i]) - int(y[i]))

print(x)
print(y)
print(z)

"""abd = []
for i in range(len(z)):
    abd.append(alphabet[i])"""

for i in range(len(z)):
    if z[i] == ' ':
        print(' ', end=' ')
        continue
    else:
        if int(z[i]) < 0:
            print(alphabet[z[i]+26], end=' ')
        else:
            print(alphabet[z[i]], end=' ')