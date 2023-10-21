###########################
### RELATIONAL OPERATOR ###
###########################

# Equal to (==)
x = 5
y = 5
print(x == y)  # True

# Not equal to (!=)
a = 10
b = 7
print(a != b)  # True

# Less than (<)
num1 = 15
num2 = 20
print(num1 < num2)  # True

# Greater than (>)
m = 30
n = 25
print(m > n)  # True

# Less than or equal to (<=)
p = 10
q = 10
print(p <= q)  # True

# Greater than or equal to (>=)
c = 8
d = 5
print(c >= d)  # True

# String number not equal to integer number
str_number = "5"
int_number = 5
print(str_number == int_number)  # False
print(str_number != int_number)  # True

# Equality using 'and' with relational operators
value1 = 12
value2 = 15
value3 = 12
print(value1 == value3 and value1 < value2)  # True

##########################
### IF/ELSE STATEMENTS ###
##########################

# Basic if statement
age = 15
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# If-else with multiple conditions
temperature = 25
if temperature > 30:
    print("It's hot outside.")
elif temperature > 20:
    print("It's warm outside.")
else:
    print("It's cool outside.")

# Using logical operators with if statements
is_raining = True
has_umbrella = False
if is_raining and not has_umbrella:
    print("You'll get wet without an umbrella.")
else:
    print("You are prepared for the rain.")

# Nested if statements
number = 0
if number > 0:
    print("Positive number")
else:
    if number < 0:
        print("Negative number")
    else:
        print("Zero")