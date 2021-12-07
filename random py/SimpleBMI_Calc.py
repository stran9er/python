# Enter your height and weight.  
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Function to calculate BMI. 
def bmi_calculator(h, w):
    height = float(h)
    weight = float (w)
    bmi_calculated = weight / (height * height)
    
    return int (bmi_calculated)

# Set a variable to hold our BMI based on input. 
bmi_calculated = bmi_calculator(height, weight)

bmi_result = ''

if bmi_calculated < 18.5:
    bmi_result = "Underweight"
elif bmi_calculated > 18.5 and bmi_calculated< 24.9:
    bmi_result = "Normal Weight"
elif bmi_calculated > 25 and bmi_calculated < 29.9:
    bmi_result = "Overweight"
else:
    bmi_result = "Obese."

# The result, lets keep us honest.  Holidays are here.
print (f"Your BMI is:  {bmi_calculated}.  You are categorized as: {bmi_result}")
