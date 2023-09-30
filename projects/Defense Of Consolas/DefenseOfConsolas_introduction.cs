Console.WriteLine("Hello, World!");

// CONVENTIONS
// -----------------------
// camelCase - First letter lower case all else upper case.
// PascalCase - First letter upper case all else upper case.
// snake_case - Words separated by underscores.

// All are valid ways to name variables, but it's a good
// practice to follow language specific conventions.

// DATA TYPES
// -----------------------
// In C# we have to declare the data type of our variables.
// Some common examples
string a = "1";
int b = 1;
double c = 1.00;
bool d = true;

// WRITING TO TERMINAL
// ----------------------
Console.WriteLine(a);
Console.WriteLine(b);
Console.WriteLine(c);
Console.WriteLine(d);

Console.WriteLine(a.GetType());
Console.WriteLine(b.GetType());
Console.WriteLine(c.GetType());
Console.WriteLine(d.GetType());

// ADDING VARIABLES TOGETHER
Console.WriteLine(a + b);

// Above command prints 11.. why? In this example the C# interpreter
// converted the integer 'b' to a string for us and concatenated the
// strings. Which we will cover in a moment. 

// CORRECTION
int ab = Convert.ToInt32(a) + b;
Console.WriteLine(ab);

// STRING INTERPOLATION
// -----------------------
string adjective = "fun";
string verb = "build";

string output1 = "Programmng is so " + adjective + ". What should we " + verb + "?";
Console.WriteLine(output1);

string output2 = String.Format("Programming is so {0}. What should we {1}?", adjective, verb);
Console.WriteLine(output2);
    
string output3 = $"Programming is so {adjective}. What should we {verb}?";
Console.WriteLine(output3);

// USER INPUT
// -----------------------
Console.WriteLine("Provide an adjective: ");
string userAdjective = Console.ReadLine();

Console.WriteLine("Provide a verb: ");
string userVerb = Console.ReadLine();

string output4 = $"Programming is so {userAdjective}. What should we {userVerb}?";
Console.WriteLine(output4);

// CONSOLE FUNCTIONS
Console.Beep();
Console.BackgroundColor = ConsoleColor.Cyan;
Console.ForegroundColor = ConsoleColor.Black;

// FUNCTIONS / PUTTING IT TOGETHER
// --------------------------------
static void MadLibs()
{
    Console.WriteLine("Provide an adjective: ");
    string userAdjective = Console.ReadLine();

    Console.WriteLine("Provide a verb: ");
    string userVerb = Console.ReadLine();

    Console.WriteLine("From the function!");
    string output = $"Programming is so {userAdjective}. What should we {userVerb}?";
    Console.WriteLine(output);
}

MadLibs();