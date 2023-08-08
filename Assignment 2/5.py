# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
class String:
    def __init__(self):
        self.a=str(input("Enter a string"))
    def getString(self):
        print("The given string is",self.a)
    def printString(self):
        print("The uppercase string is",self.a.upper())

s1=String()
s1.getString()
s1.printString()