# Python Program to Update 
# character of a String

String1 = "Hello World!"
list1 = list(String1)
list1[2] = 'p'
String2 = "".join(list1)
print(String2)

# Other method to update a character using slicing method

newString = "Hella World!"
newString2 = newString[:4] + 'o' + newString[5:]
print(newString2.upper())
