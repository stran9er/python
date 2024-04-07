#Function to print random stars
def Stars(n: int):
    # Variable to hold our stars, initiated as blank space.
    str = ""

    for i in range(n):
        # Append our string with a star.
        str +="*"
        print(str)


# Call function and set to user feedback. 
print(f"User input based:\n")
Stars(int(input("How many stars do you want?")))

# Set a value that the programmer or system assigns
print("\nSystem based:\n")
Stars(5)

# Sets a random value from the range.
print("\nRandom Set:\n")
import random as rnd
rnd_range = rnd.randint(0,100+1)
Stars(rnd_range)
