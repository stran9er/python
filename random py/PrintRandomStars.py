# Function to print random stars
def Stars(n: int):
    # Variable to hold our stars, initiated as blank space.
    str = ""

    for i in range (n):
        # Append our string with a star.
        str +="*"
        print(str)

# Call the function and set to 5.
Stars(5)
