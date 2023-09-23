// ###############################################################
// - Girls Who Code					                                     #
// - Password Generator         	                               #
// - Lesson - 5 | Add a function to restart the generator.       #
// ###############################################################

// 1. Add the following code after the "report settings to users"
//    section in main.cpp

// .. rest of code above
bool restartGenerator = entry.getYesNoInput("\nGenerate another password");
if (restartGenerator)
{
  system("clear"); // Linux/Mac
  // system("cls"); // Windows

  main();
}