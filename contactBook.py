import os
fileName = 'contacts.csv'
def createFileIfDosentExist():
	if os.path.exists(fileName) == False:
		file = open(fileName, 'x')
		file.close()

def addContact():
	firstName = input('What is the contacts first name')
	lastName = input('What is the contacts last name')
	email = input('What is the contacts email')
	phoneNum = input('What is the contacts phone number')
	contactInfo = firstName + ',' + lastName + ',' + email + ',' + phoneNum
	if isFileEmpty() == False:
		contactInfo = '\n' + contactInfo
	file = open(fileName, 'a')
	file.write(contactInfo)
	file.close()

def viewContacts():
	file = open(fileName, 'r')
	emptyFile = True
	for line in file:
		emptyFile = False
		line = line.strip('\n')
		firstName, lastName, email, phoneNum = line.split(',')
		print('Name: ' + firstName + ' ' + lastName + '\nEmail: ' + email + '\nNumber: ' + phoneNum + '\n')	
	if emptyFile == True:
		print('No contacts found')
	file.close()

def isFileEmpty():
	emptyFile = False
	if os.path.getsize(fileName) == 0:
		emptyFile = True
	return emptyFile

createFileIfDosentExist()

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
		addContact()
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