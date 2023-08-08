# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
num=int(input('Enter a number'))
ans=1
for i in range(1,num+1):
    ans=ans*i
print(ans)