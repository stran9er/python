def announce(f):  #this function modifies the input (f)
	def wrapper():
		print ("About to run the function...")  #announce decorator
		f()
		print("Done with the function.")  #close decorator
	return wrapper

@announce #adds the decorator to the function below
def hello(): 
	print ("\nHello, world!")

hello()

