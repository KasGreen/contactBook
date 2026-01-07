continueContactBook = True
while continueContactBook == True:
	valid_user_option = False
	while valid_user_option == False:
		try:
			user_option = int(input('''Would you like to: 
1: Add a new contact
2: Delete a contact
3: View all contacts
4: Exit the program
'''))
		except:
			print('Please enter a number')
			continue
		if user_option < 1 or user_option > 4:
			print('Please enter a valid number')
		else:
			valid_user_option = True

	if user_option == 1:
		print('option 1')
	elif user_option == 2:
		print('option 2')
	elif user_option == 3:
		print('option 3')
	elif user_option == 4:
		print('option 4')

	validAnswer = ''
	while validAnswer != 'y' and validAnswer != 'n':
		validAnswer = input('Would you like to select anothor option y/n: ')
		if validAnswer == 'y':
			break
		if validAnswer == 'n':
			continueContactBook = False