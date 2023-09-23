# Madlibs Game

_This is a very simple game that will introduce the concepts of variables, string concatenation, and user input._
<br>

## Intro to Variables

Use this lesson to show a demo of printing a string from the console
<br>

```
my_string = "GWC"
```

## Intro to String Concatenation

First ask the students if they know what string concatenation is and provide the answer if not.
<br>

In Python there are many a few ways to concatenate strings

```
print("we love " + my_string)
print("we love {}".format(my_string))
print(f"we love {my_string}")
```

## Intro to User Input

Now we know how to format a string and create variables, but for a Madlibs style game we need the allow the user to create there own variables.<br>
**Question:** Does anyone know how to do this?<br>
**Answer:** User input
<br>

Python has a built in function called input() that can read the text a user enters into the terminal. It also accepts a string parameter that will be displayed to the user.

```
adjective = input("Adjective: ")
verb = input("Verb: ")

print(adjective)
print(verb)
```

## Final Result

```
adjective = input("Adjective: ")
verb = input("Verb: ")
madlib = f"Computer programming is so {adjective}! It makes me so excited all the time because I love to {verb}!"

print(madlib)
```
