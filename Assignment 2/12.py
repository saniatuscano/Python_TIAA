# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
ans=[]

def check(n):
    for x in str(n):
        if int(x)%2!=0:
            return False
    return True

for i in range(1000,3001):
    if check(i):
        ans.append(i)

print(ans)
