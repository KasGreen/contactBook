import os
import sys

if __name__ == '__main__':
	print('error: can not be run as main module')
	sys.exit(1)

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

def deleteContact():
	contactToDelete = input('enter the phone number of the contact you want to delete')
	if isFileEmpty() == True:
		print('No contacts found')
		return
	file = open(fileName, 'r')
	lines = []
	for line in file:
		line = line.strip('\n')
		lines.append(line)
	for i in range (0, len(lines)):
		firstName, lastName, email, phoneNum = lines[i].split(',')
		if contactToDelete == phoneNum:
			lines.pop(i)
			break			
	file.close()
	file = open(fileName, 'w')
	for i in range(0, len(lines)):
		if i > 0:
			file.write('\n' + lines[i])
		else:
			file.write(lines[i])
	file.close()


def viewContacts():
	if isFileEmpty() == True:
		print('No contacts found')
	file = open(fileName, 'r')
	for line in file:
		line = line.strip('\n')
		firstName, lastName, email, phoneNum = line.split(',')
		print('Name: ' + firstName + ' ' + lastName + '\nEmail: ' + email + '\nNumber: ' + phoneNum + '\n')	
	file.close()

def isFileEmpty():
	emptyFile = False
	if os.path.getsize(fileName) == 0:
		emptyFile = True
	return emptyFile