from CBpackages import CBeditor as cbe
import sys

if __name__ != '__main__':
	print('Error: must be run as main module')
	sys.exit(1)

def programExit():
	print('Bye')
	sys.exit(0)

cbe.createFileIfDosentExist()

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
		cbe.addContact()
	elif userOption == 2:
		cbe.deleteContact()
	elif userOption == 3:
		cbe.viewContacts()
	elif userOption == 4:
		programExit()

	validAnswer = ''
	while validAnswer != 'y' and validAnswer != 'n':
		validAnswer = input('Would you like to select another option y/n: ')
		if validAnswer == 'y':
			break
		if validAnswer == 'n':
			continueContactBook = False
programExit()