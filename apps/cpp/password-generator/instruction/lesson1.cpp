// ###############################################################
// - Girls Who Code					                                     #
// - Password Generator         	                               #
// - Lesson - 1 | Intro to C++ & capturing user input     		   #
// ###############################################################

// Instructors: Comment out code blocks between START COMMENT # &
//              END COMMENT # to demo each main method.

// 1. Basic user input.
// START COMMENT 1
#include <iostream>
using namespace std;

int main()
{
  int passwordLength;

  cout << "\n\nC++ PASSWORD GENERATOR\n\n";
  cout << "Desired password length (integer): ";
  cin >> passwordLength;

  cout << "User entered " << passwordLength << ".\n\n";
  cout << "\n";
  return 0;
}
// END COMMENT 1
// This lets user enter non-numeric numbers which is not what we want,
// so we must revise the main method.

// 2. Require users to input numbers.
// START COMMENT 2
#include <iostream>
#include <limits>
using namespace std;
int main()
{
  int passwordLength;
  bool isValid = false;

  cout << "\n\nC++ PASSWORD GENERATOR\n\n";

  // Continue asking until input is valid.
  while (!isValid)
  {
    cout << "Desired password length (integer): ";
    cin >> passwordLength;

    // Check that all input in line are an integer.
    if (cin.fail() || cin.peek() != '\n')
    {
      // Ask again.
      cout << "Invalid input! Enter an integer: \n";
      // Clear previous entry & prevent infinite loop.
      cin.clear();
      cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }
    else
    {
      isValid = true;
    }
  }
  cout << "User entered " << passwordLength << ".\n\n";
  cout << "\n";
  return 0;
}
// END COMMENT 2