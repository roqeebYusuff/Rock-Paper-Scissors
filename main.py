# import random module
import random

while True: 
	# List of all possible options
	ans = ['R', 'P', 'S']

	print("Select an option \n R for Rock, \n P for paper, and \n S for scissor \n")
	
	# prompt player to select am option
	option = input("Player's turn: ")
	
	# loop until player enter invalid option
	while option not in ans:
		print('\nOoooops...Invalid option entered\n')
		option = input("Select a valid option: ")

	if option == 'R':
		option_name = 'Rock'
	elif option == 'P':
		option_name = 'Paper'
	else:
		option_name = 'Scissors'
		
	# print player option
	print("Player's option is: " + option_name)
	print("\nCPU's turn.......")

	# CPU picks a random option from the list
	cpu_option = random.choice(ans)
	
	# If its a tie, reload
	while cpu_option == option:
		cpu_option = random.choice(ans)

	if cpu_option == 'R':
		cpu_option_name = 'Rock'
	elif cpu_option == 'P':
		cpu_option_name = 'Paper'
	else:
		cpu_option_name = 'Scissors'
		
	print("CPU's option is: " + cpu_option_name)

	print('\nPlayer (', option_name, '): CPU(', cpu_option_name, ')\n' )

	# Check if it's a tie
	if option == cpu_option:
		result = 'Draw'
	
	# Paper covers rock
	elif((option == 'R' and cpu_option == 'P') or (option == 'P' and cpu_option =='R' )):
		result = "Paper"
	
	# Rock breaks scissors
	elif((option == 'R' and cpu_option == 'S') or (option == 'S' and cpu_option == 'R')):
		result = "Rock"
	
	# Scissors cuts paper
	else:
		result = "Scissors"

	# Printing either user or computer wins or draw
	if result == 'Draw':
		print("It's a tie")

	elif result == option_name:
		print("Player wins")

	elif result == cpu_option_name:
		print("CPU wins")
		
	break