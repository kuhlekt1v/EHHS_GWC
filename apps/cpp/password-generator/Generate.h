#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;

class Generate
{
public:
  Generate() { srand(time(nullptr)); }

  static char randomInteger();
  static char randomSpecial();
  static char randomLetter(string type);
};

// Generate random number 0-9
char Generate::randomInteger()
{
  int number = rand() % 10;
  return static_cast<char>(number);
}

// Generate a random special character
char Generate::randomSpecial()
{
  string specialCharacters = "!@#$%^&*()?";
  int randomIndex = rand() % specialCharacters.length();
  return specialCharacters[randomIndex];
}

char Generate::randomLetter(string type)
{
  // Generate a random between 0-25
  int randomInteger = rand() % 26;

  char randomLetter;
  if (type == "lower")
  {
    randomLetter = 'a' + randomInteger;
  }
  else if (type == "upper")
  {
    randomLetter = 'A' + randomInteger;
  }
  return randomLetter;
}
