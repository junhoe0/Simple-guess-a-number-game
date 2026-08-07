import random
art = '''⠀⠀⢀⠤⣂⣤⣬⣭⣭⣭⣔⡠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠔⣵⣾⣿⣿⣿⢿⣿⣿⣿⣿⣎⢂⠀⢲⣤⣤⣤⣤⣀⣒⣒⣒⣒⣂⡠⠤⠤⣄
⠐⣾⣿⣿⣿⡏⣾⡿⢎⣛⣫⣭⣴⣾⠆⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢼
⡇⣿⣿⣿⣿⣟⡿⢀⣐⣻⣛⡩⢁⠀⠀⣘⣛⣛⡛⠿⠿⠿⢿⣿⣿⣿⣿⣿⢟⣾
⡇⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣶⡕⠄⠉⠛⠛⠛⠛⡻⣣⣾⣿⣿⣿⢟⣵⣿⠛
⠃⣿⣿⣿⣿⣿⢋⣥⠭⡻⣿⣿⣿⣿⡌⡄⠀⠀⠀⡐⣼⣿⣿⣿⡿⣣⣾⠏⠀⠀
⠨⢻⣿⣿⣿⣧⢻⠁⠀⠘⢸⣿⣿⣿⡇⣿⠀⠀⠌⣼⣿⣿⣿⡿⢱⣿⠃⠀⠀⠀
⠀⢦⢻⣿⣿⣿⣦⣐⣀⣊⣼⣿⣿⡿⢱⡿⠀⠰⣸⣿⣿⣿⣿⢣⣿⠃⠀⠀⠀⠀
⠀⠀⠣⣙⠿⣿⣿⣿⣿⣿⣿⠿⢛⣵⡿⠃⢀⢃⣿⣿⣿⣿⡟⣾⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠛⠶⣮⣭⣭⣴⣶⡿⠿⠋⠀⠀⢨⣘⣿⡻⠿⠿⢇⣿⠀⠀⠀⠀⠀⠀
⠀⠀⢀⠔⠒⠂⠠⠤⠭⡀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠛⠛⠻⠃⠀⠀⠀⠀⠀⠀
⢀⠆⠁⠀⡄⠀⠀⠀⠀⠈⢂⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠒⠁⠀⠀⠒⢤⡀⠀⠀
⠣⠤⢤⠞⠂⠀⣀⠰⠃⠀⠘⣆⢀⣀⠀⠀⠀⠀⢀⠎⠀⢠⡀⠀⠀⠀⢀⠀⠙⡀
⠀⠀⢸⠀⠈⠭⡀⢈⣡⠔⢶⠁⣹⢩⠃⠀⢀⠀⢸⠀⠀⠀⣑⣠⣤⠀⠙⡦⣀⠜
⠀⠀⠀⠣⠀⢂⠞⠱⠴⣈⡸⠰⢇⠘⠀⠰⡭⠷⢝⡤⣂⣄⠒⢤⡐⠀⠀⡇⠀⠀
⠀⠀⠀⠀⠱⠄⣀⢜⢁⡠⠥⠊⠀⠀⠀⠀⠡⡘⡄⠐⡂⠘⢌⡀⠉⠂⡸⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠄⠹⢅⣀⠹⠒⠊⠀⠀⠀ '''


print('\n---Number guessing game by Jun Hoe---\n')
gamebool= False
easybool = False
hardbool = False
print('Tip : To use hints, type hint (only for hard mode)\nYou have been given a free hint')
hints = 0
hints += 1
tries = 0
coins = 0
shop = {
    'hints': {
        'price': '15'
    },
    'placeholder': {
        'price': '0'
    }
}

class shopitems:
    def __init__(self, name, price):
        self.name = name
        self.price = price

items = {}

for name, data in shop.items():
    items[name] = shopitems(name, data['price'])
    
def calcucoins():
    global tmpcoins
    tmpcoins = 0
    if tries <=10:
        tmpcoins += random.randint(15,18)
    elif tries > 10 and tries <= 20:
        tmpcoins += random.randint(9, 12)
    elif tries > 20 and tries <= 50:
        tmpcoins += random.randint(5, 8)
    elif tries > 50:
        tmpcoins += random.randint(2, 4)
    return tmpcoins 

while True:
    print('\n--Main Menu--\n')
    print('1. Start Game\n2. Shop\n3. Exit')
    user = input('\n> ')

    if user == '1':
        gamebool = True
    elif user == '2':
        print('\n--Shop--\n')
        print(list(shop))
        print(f'\nCoins: {coins}')
        input('\nEnter to continue..')
    elif user == '3':
        break
    else:
        print('\nPlease choose a number')
        input('Enter to continue...')
    
    while gamebool:
        
        while True:
            mode = input('\nSelect mode [easy] [hard]:\n> ').strip().lower()
            if mode == 'e' or mode == 'easy':
                easybool = True
                hardbool = False
                break
            elif mode == 'hard' or mode == 'h':
                easybool = False
                hardbool = True
                break
            else:
                hardbool = easybool = False
                print('Please choose one\n')

        lives = 10
               
        while True:
            print('\nGive a maximum value')
            inputmaxvalue = input().strip().lower()
            try:
                #global maxvalue
                maxvalue = int(inputmaxvalue)
                break
            except:
                print('Please type a number\n')
        x = random.randint(0, maxvalue)
        
        print('\nGood Luck\n\nGuess a number:\n')

        while easybool:
            tries += 1
            userinput = input('> ').strip().lower()
            if userinput == 'exit' or userinput == 'quit':
                break
            try:
                #global numbereasy
                numbereasy = int(userinput)
            except:
                print('Please type a number\n')
                continue
            if numbereasy == 67 and numbereasy != x:
                print(art)
            match x:
                case _ if numbereasy < x:
                    print('higher\n')
                case _ if numbereasy > x:
                    print('lower\n')
                case _ if numbereasy == x:
                    print(f'You won! (In {tries} tries)')
                    calcucoins()
                    print(f'Coins earned: {tmpcoins}')
                    coins += tmpcoins
                    tmpcoins = 0
                    tries = 0
                    break

        while hardbool:
            tries += 1
            print(f'Hints = {hints}')
            print(f'Lives = {lives}\n')
            userinput = input('> ').lower().strip()
            if userinput == 'exit' or userinput == 'quit':
                break
            if userinput == 'hint' and hints > 0:
                if maxvalue <= 20:
                    befX = x - random.randint(2, 4)
                    aftX = x + random.randint(2, 4)
                elif maxvalue > 20:
                    befX = x - random.randint(7, 10)
                    aftX = x + random.randint(7, 10)
                if aftX > maxvalue:
                    diff = aftX - maxvalue
                    aftX = aftX - diff
                elif befX < 0:
                    befX = 0
                print(f'Number is between {befX} and {aftX}\n')
                hints -= 1
            elif hints == 0:
                print('You have no more hints left\n')
            try:
                #global numberhard
                numberhard = int(userinput)
            except:
                print('Please type a number\n')
                continue
            if numberhard == 67 and numberhard != x:
                print(art)
            match x:
                case _ if numberhard < x:
                    print('higher\n')
                    lives -= 1
                case _ if numberhard > x:
                    print('lower\n')
                    lives -= 1
                case _ if numberhard == x:
                    print(f'\nYou won! (In {tries} tries)')
                    calcucoins()
                    coins += tmpcoins
                    tmpcoins = 0
                    tries = 0
                    break
            if lives == 0:
                print('\nOut of lives :(')
                print(f'It was {x}\n')
                break

        replayinput = input("\nContinue playing? (y/n) : \n> ")
        if replayinput == 'y':
            continue
        elif replayinput == 'n':
            print('\nGoing back to main menu...\n')
            break
