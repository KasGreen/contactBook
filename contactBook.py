import os
def viewContacts():
	FileName = 'contacts.csv'
	file = open(FileName, 'r')
	for line in file:
		line = line.strip('\n')
		firstName, lastName, email, phoneNum = line.split(',')
		print('Name: ' + firstName + ' ' + lastName + '\nEmail: ' + email + '\nNumber: ' + phoneNum + '\n')	

	file.close()



continueContactBook = True
while continueContactBook == True:
	validUserOption = False
	while validUserOption == False:
		try:
			userOption = int(input('''Would you like to: 
1: Add a new contact
2: Delete a contact
3: View all contacts
4: Exit the program
'''))
		except:
			print('Please enter a number')
			continue
		if userOption < 1 or userOption > 4:
			print('Please enter a valid number')
		else:
			validUserOption = True

	if userOption == 1:
		print('option 1')
	elif userOption == 2:
		print('option 2')
	elif userOption == 3:
		viewContacts()
	elif userOption == 4:
		print('option 4')

	validAnswer = ''
	while validAnswer != 'y' and validAnswer != 'n':
		validAnswer = input('Would you like to select anothor option y/n: ')
		if validAnswer == 'y':
			break
		if validAnswer == 'n':
			continueContactBook = False