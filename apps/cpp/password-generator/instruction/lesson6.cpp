// ###############################################################
// - Girls Who Code                                              #
// - Password Generator                                          #
// - Lesson - 6 | Add a class "Generate" for all character       #
//                generator methods                              #
// ###############################################################

// 1. Create a new file "Generate.h"
//    * Define method to generate random integer.
//    * Define method generate random special char.
//    * Define method to generate random letter
//    * Demo and point out same letter issue.

#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;

class Generate
{
public:
  // DEMO WITH & WITHOUT THIS INITIALIZATION.
  // Upper and lower always the same 2 values.

  // Seed Generate class with a random starting number based
  // on the current time. Starting will always be different
  // provided class is not initialized multiple times in 1
  // second.
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

// 2. Update "main.cpp" to use Generate.h & provide demo before the
//    re-run generator prompt.
#include "Generate.h"
Generate generate;

// .. Code truncated.
int number = generate.randomInteger();
char special = generate.randomSpecial();
char upper = generate.randomLetter("upper");
char lower = generate.randomLetter("lower");

cout << number;
cout << special;
cout << upper;
cout << lower;
