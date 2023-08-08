# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
import re
sentence=input("enter").split()
letters=0
digits=0

for word in sentence:
    for char in word:
        if char.isalpha()==True:
            letters+=1
        elif char.isnumeric()==True:
            digits+=1
        else:
            continue
      
print("Letters",letters)
print("Digits",digits)

