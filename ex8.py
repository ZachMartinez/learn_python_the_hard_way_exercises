# Create a string with four formatter slots.
formatter = "{} {} {} {}"

# Print formatter string with the numbers 1-4.
print(formatter.format(1, 2, 3, 4))
# Print formatter string with string for the first four ordinal numbers
# passed to it.
print(formatter.format("one", "two", "three", "four"))
# Print formatter string with four booleans passed into it.
print(formatter.format(True, False, False, True))
# Print formatter string with itself passed into it four times.
print(formatter.format(formatter, formatter, formatter, formatter))
# Print formatter string with four sentence strings passed into it.
print(formatter.format(
    "I do not aim with my hand.",
    "I aim with my eye.",
    "I do not kill with my gun.",
    "I kill with my heart."
))
