# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
n=input("enter a number")
n1=n*1
n2=n*2
n3=n*3
n4=n*4
print(int(n1)+int(n2)+int(n3)+int(n4))
