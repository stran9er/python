''' 
	Created to help friends understand the importance of strong passwords, 
	by illustrating how easy it is to find their passwords in any password
	dictionary available online. 

	Author:  Tarric Ali

'''

filename = 'rockyou.txt'				# The name of the text file to be used.  
passCheck =""					 	# Flag holder for the loop.

while passCheck !='quit':				# A loop to allow multiple passwords to be checked in one instance. It stops when 'quit' is entered.

	passCheck = input("Enter a password to check or 'quit' to stop: ")

	if passCheck in open (filename, encoding='UTF-8', errors='ignore').read():
		print(f"Your password, '{passCheck}' WAS found int eh list.")

	else:
		print(f"Your password was NOT found in the list.")
