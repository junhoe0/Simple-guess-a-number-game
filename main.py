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
easybool = False
hardbool = False

while True:
	while True:
		mode = input('Select mode [easy] [hard]:\n')
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
		
	lives = 5
	while True:
		print('\nGive a maximum value')
		inputmaxvalue = input()
		try:
			global maxvalue
			maxvalue = int(inputmaxvalue)
			break
		except:
			print('Please type a number\n')
	x = random.randint(0, maxvalue)
	print('\nGood Luck\n\nGuess a number:\n')

	while easybool:
		userinput = input()
		if userinput == 'exit' or userinput == 'quit':
			break
		try:
			global numbereasy
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
				print('You won!')
				break

	while hardbool:
		print(f'lives = {lives}')
		userinput = input()
		if userinput == 'exit' or userinput == 'quit':
			break
		try:
			global numberhard
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
				print('\nYou won!')
				break
		if lives == 0:
			print('\nOut of lives :(')
			print(f'It was {x}\n')
			break
	replayinput = input("\nContinue playing? (y/n) : ")
	print('')
	if replayinput == 'y':
		continue
	elif replayinput == 'n':
		print('Bye')
		break
