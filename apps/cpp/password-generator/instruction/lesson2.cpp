// ###############################################################
// - Girls Who Code					                                     #
// - Password Generator         	                               #
// - Lesson - 2 |  Move passwordLength function to own file      #
// ###############################################################

// 1. Move passwordlength to own file.
//    * Create new file "passwordLength.h"

// START passwordLength.h
#include <iostream>
#include <limits>

using namespace std;

int passwordLength()
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
// END passwordLength.h

// 2. Update main.cpp

// START updated main.cpp
#include "passwordLength.h"

int main()
{
  cout << "\n\nC++ PASSWORD GENERATOR\n\n";

  int length = passwordLength();

  cout << "User entered " << length << ".\n\n";
  cout << "\n";
  return 0;
}
// END updated main.cpp