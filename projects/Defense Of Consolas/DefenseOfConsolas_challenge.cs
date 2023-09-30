Console.Title = "Defense of Consolas";

Console.Write("Target Row? ");
int row = Convert.ToInt32(Console.ReadLine());

Console.Write("Target Column? ");
int column = Convert.ToInt32(Console.ReadLine());

Console.ForegroundColor = ConsoleColor.Yellow;

DeployDefenses(row, column);

Console.Beep();

static void DeployDefenses(int row, int column)
{
    Console.WriteLine("Deploy to:");
    Console.WriteLine($"({row}, {column - 1})");
    Console.WriteLine($"({row - 1}, {column})");
    Console.WriteLine($"({row}, {column + 1})");
    Console.WriteLine($"({row + 1}, {column})");
}