// ###############################################################
// - Girls Who Code                                              #
// - Password Generator                                          #
// - Lesson - 3 |  Move passwordLength function to own class     #
// ###############################################################

// 1. Move passwordLength to a UserEntry class.
//    * Create new file "UserEntry.h"
//    * When finished delete "passwordLength.h"
//    * Update main.cpp

// START "UserEntry.h"
#include <iostream>
#include <cstdlib>
#include <limits>

using namespace std;

class UserEntry
{
public:
  static int passwordLength();
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
// END "UserEntry.h"

// 2. Update main.cpp

// START "main.cpp"
#include "UserEntry.h"

int main()
{
  // Initialize user entry class.
  UserEntry entry;

  cout << "\n\nC++ PASSWORD GENERATOR\n\n";

  int length = entry.passwordLength();

  cout << "User entered " << length << ".\n\n";
  cout << "\n";
  return 0;
}
// END "main.cpp"
