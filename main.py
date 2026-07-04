import random

print('Give a maximum value')
maxvalue = int(input())
x = random.randint(0, maxvalue)
print('''Number guessing game by Jun Hoe
Good Luck

Guess the number:''')

while True:
    userinput = int(input())
    
    if userinput == 12456:
        break
    match x:
        case _ if userinput < x:
            print('higher')
        case _ if userinput > x:
            print('lower')
        case _ if userinput == x:
            print('You won!')
            break
    print('')
