// ###############################################################
// - Girls Who Code					                                     #
// - Password Generator         	                               #
// - Lesson - 7 | Add a function to create the randomized        #
//                password based on user input and finish        #
//                main program                                   #
// ###############################################################

// 1. Add include statement to top of main.cpp
#include <vector>

// 2. Add generatePassword function above main function in main.cpp
string generatePassword(bool upper, bool lower, bool number, bool special,
                        int length)
{
  Generate generate;
  string password = "";
  vector<string> types;

  // If no types specified return empty string;
  int typesCount = upper + lower + number + special;
  if (typesCount == 0)
  {
    return password;
  }

  // Define types of characters to include in the password.
  if (upper)
  {
    types.push_back("upper");
  }
  if (lower)
  {
    types.push_back("lower");
  }
  if (number)
  {
    types.push_back("number");
  }
  if (special)
  {
    types.push_back("special");
  }

  // Generate password
  for (int i = 0; i < length; i++)
  {
    // Choose random type from available types
    int randomTypeIndex = rand() % types.size();
    string randomType = types[randomTypeIndex];

    // Generate random character based on chosen type
    string randomChar;
    if (randomType == "upper")
    {
      randomChar = generate.randomLetter("upper");
    }
    else if (randomType == "lower")
    {
      randomChar = generate.randomLetter("lower");
    }
    else if (randomType == "number")
    {
      int randomInt = generate.randomInteger();
      randomChar = to_string(randomInt);
    }
    else if (randomType == "special")
    {
      randomChar = generate.randomSpecial();
    }

    // Add random character to password
    password += randomChar;
  }

  return password;
}

// 3. Update main.cpp
int main()
{
  UserEntry entry;
  Generate generate;

  cout << "\n\nC++ PASSWORD GENERATOR\n\n";

  int length = entry.passwordLength();

  bool includeUpper = entry.getYesNoInput("Include uppercase letters");
  bool includeLower = entry.getYesNoInput("Include lowercase letters");
  bool includeNumber = entry.getYesNoInput("Include numbers");
  bool includeSpecial = entry.getYesNoInput("Include special characters");

  // Report settings to users
  cout << "\nPASSWORD SETTINGS\n";
  cout << "Length: " << length;
  cout << "\nUppercase: " << boolToString(includeUpper);
  cout << "\nLowercase: " << boolToString(includeLower);
  cout << "\nNumbers: " << boolToString(includeNumber);
  cout << "\nSymbols " << boolToString(includeSpecial);

  cout << "\n\n--- GENERATED PASSWORD ---\n";

  string password = generatePassword(includeUpper, includeLower,
                                     includeNumber, includeSpecial, length);

  cout << password;

  bool restartGenerator = entry.getYesNoInput("\n\nGenerate another password");
  if (restartGenerator)
  {
    system("clear"); // Linux/Mac
    // system("cls"); // Windows
    main();
  }

  return 0;
}
