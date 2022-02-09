
print('\nTHE EUCLIDEAN ALGORITHM \n\n\tSTART \n')

# START
while True:
    # Insert values of a and b
    a = input('Insert a:')
    b = input('Insert b:')
    # a and b are numbers?
    if a.isnumeric() and b.isnumeric():
        # cast values a and b
        a = int(a)
        b = int(b)
        # exit of loop
        break
    # Message of error 
    print('ERROR... input values are not numbers')
print()

# a > b ?
if a < b:
    # Swap a and b
    a, b = b, a

print(' {:7} {:7} {:7} {:7}'.format('Dividend', 'Divisor', 'Quotient', 'Remainder'))
printValues = False
aux = 0
while True:
    # Divide a by b calling the remainder r
    c = a // b
    aux = b # GCD is the final value of b
    r = a % b
    print('{:9}  / {:9} {:9} {:9}'.format(a, b, c, r))
    # Replace a with b
    a = b
    # replace b with r
    b = r
    # r > 0 ?
    if r <= 0:
        break

print('\nGCD: ', aux)
#print('NO SON PRIMOS' if aux==0 else 'SON PRIMOS')
print('\n\tEND')


