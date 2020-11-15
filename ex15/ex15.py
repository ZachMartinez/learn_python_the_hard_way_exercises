#Get the argv object from the sys module
from sys import argv

#Take one argument assign to variable filename
script, filename = argv
#Use input instead of argv
# print("Enter the name of the file you want to open")
# filename = input("> ")

#Assign file object to variable txt
txt = open(filename)

#Print message with filename
print(f"Here's your file {filename}:")
#Print text file data to terminal
print(txt.read())
txt.close()
