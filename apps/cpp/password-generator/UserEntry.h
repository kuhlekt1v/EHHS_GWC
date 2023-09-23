#include <iostream>
#include <cstdlib>
#include <limits>

using namespace std;

class UserEntry
{
public:
  static int passwordLength();
  static bool getYesNoInput(string prompt);
};

int UserEntry::passwordLength()
{
  int passwordLength;
  bool isValid = false;

  // Continue asking until input is valid.
  while (!isValid)
  {
    cout << "Desired password length (integer): ";
    cin >> passwordLength;

    // Check that user input is integer.
    if (cin.fail() || cin.peek() != '\n')
    {
      // Ask again.
      cout << "Invalid input! Enter an integer: ";
      cin.clear();
      cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }
    else
    {
      isValid = true;
    }
  }
  return passwordLength;
}

bool UserEntry::getYesNoInput(string prompt)
{
  string input;

  do
  {
    cout << prompt << ":\n";
    cout << "Enter 'y' for yes or 'n' for no: ";
    cin >> input;
  } while (input != "y" && input != "n");

  return (input == "y");
}