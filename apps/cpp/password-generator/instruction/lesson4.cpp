// ###############################################################
// - Girls Who Code					                                     #
// - Password Generator         	                               #
// - Lesson - 4 | Yes/No user option decisions            		   #
// ###############################################################

// 1. Define public member getYesNoInput
class UserEntry
{
public:
  static int passwordLength();
  // Add this.
  static bool getYesNoInput(string prompt);
};

// 2. Add getYesNoInput method to end of UserEntry class.
bool UserEntry::getYesNoInput(string prompt)
{
  string input;

  // Continue y/n input prompt until either y or n is pressed.
  do
  {
    cout << prompt << ":\n";
    cout << "Enter 'y' for yes or 'n' for no: ";
    cin >> input;
  } while (input != "y" && input != "n");

  // Return true if input = y else return false.
  return (input == "y");
}

// 3. Update main.cpp to capture all user options.
//    * Run the app and demonstrate to students booleans.
//      0 & 1 instead of Y/N.
#include "UserEntry.h"

int main()
{
  // Initialize user entry class.
  UserEntry entry;

  cout << "\n\nC++ PASSWORD GENERATOR\n\n";

  // Save user requirements to variables.
  int length = entry.passwordLength();
  bool includeUpper = entry.getYesNoInput("Include uppercase letters");
  bool includeLower = entry.getYesNoInput("Include lowercase letters");
  bool includeNumber = entry.getYesNoInput("Include numbers");
  bool includeSpecial = entry.getYesNoInput("Include special characters");

  // Report settings to users.
  cout << "\nPASSWORD SETTINGS\n";
  cout << "Length: " << length;
  cout << "\nUppercase: " << includeUpper;
  cout << "\nLowercase: " << includeLower;
  cout << "\nNumbers: " << includeNumber;
  cout << "\nSymbols " << includeSpecial;
  cout << "\n";
  return 0;
}

// 4. Create a helper function to convert 0/1 to y/n
//    * Add boolToString above int
//    * Wrap variables in boolToString
#include "UserEntry.h"

string boolToString(int input)
{
  if (input == 1)
    return "Yes";

  return "No";
}

int main()
{
  // ... Code truncated

  // Wrap variables example.
  cout << "\nUppercase: " << boolToString(includeUpper);
  // ... Code truncated, but to do the same to all variable except length.