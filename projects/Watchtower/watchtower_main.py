# Ask user for coordinates
x_input = input("X Value: ")
y_input = input("Y Value: ")

# Cast string to type. 
# Instructor Note: This step is required in Replit (2023), but newer
# versions of Python infer the type as an integer automatically. It
# is still a good practice to cast the type.

x = int(x_input)
y = int(y_input)

# Print the direction people are traveling from.
base_response = "\nThe people are coming from the "

if x > 0 and y > 0:
    print(base_response + "North East.")
if x == 0 and y > 0:
    print(base_response + "North.")
if x < 0 and y > 0:
    print(base_response +"North West")
if x > 0 and y == 0:
    print(base_response + "East.")
if x == 0 and y == 0:
    print("The people are here!")
if x < 0 and y == 0:
    print(base_response + "West.")
if x > 0 and y < 0:
    print(base_response + "South East.")
if x == 0 and y < 0:
    print(base_response + "South.")
if x < 0 and y < 0:
    print(base_response + "South West.")