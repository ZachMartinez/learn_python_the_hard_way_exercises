# How many types of people there are.
types_of_people = 10
# Stringception
# Create a string with types_of_people format into it.
x = f"There are {types_of_people} types of people."

# The strings for the words "binary", & "don't".
binary = "binary"
do_not = "don't"

# Stringception
# Create a string with the vars "binary" & "do_not" in it.
y = f"Those who know {binary} and those who {do_not}."

# Print strings x and y.
print(x)
print(y)

# Stringception
# Print string x and y formatted withing new strings.
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Set var hilarious to False.
hilarious = False

# Create a format string with an empty space for a value.
joke_evaluation = "Isn't that joke so funny?! {}"

# Stringception
# Print joke_evaluation string with the hilarious var formatted into it.
print(joke_evaluation.format(hilarious))

# Create two strings.
w = "This is the left side of..."
e = "a string with a right side."

# Print both strings concatenated on one line.
print(w + e)
