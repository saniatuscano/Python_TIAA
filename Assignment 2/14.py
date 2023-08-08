# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
upper=0
lower=0
sentence=input("enter").split()

for word in sentence:
    for letter in word: 
        if letter.isupper()==True:
            upper+=1
        elif letter.islower()==True:
            lower+=1
        else:
            continue
      
print("upper",upper)
print("lower",lower)