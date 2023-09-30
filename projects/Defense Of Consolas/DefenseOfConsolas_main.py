# Provide to students
class colors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


# Get user input for row and column
row = int(input("Target Row? "))
column = int(input("Target Column? "))

# Set console color
print(f"{colors.WARNING}")

# Display deployment positions
print("Deploy to:")
print(f"({row}, {column - 1})")
print(f"({row - 1}, {column})")
print(f"({row}, {column + 1})")
print(f"({row + 1}, {column})")

# Beep sound
print('\a')
