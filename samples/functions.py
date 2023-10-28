# Introduction to Functions

# Function definition
def greet():
    print("Hello, welcome to the world of functions!")

# Function call
greet()

# Function with parameters
def square(number):
    result = number ** 2
    print(f"The square of {number} is: {result}")

# Call the square function with an argument
square(5)

# Function with return value
def add(x, y):
    sum_result = x + y
    return sum_result

# Call the add function and print the result
result = add(3, 7)
print(f"The sum is: {result}")