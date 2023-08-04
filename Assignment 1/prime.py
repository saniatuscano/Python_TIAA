prime=[]
notprime=[]
for i in range(1,50):
    if i==2:
        prime.append(2)
    else:
        for j in range(2,50):
            if i%j==0:
                break
        if i==j:    
            prime.append(i)
                
print(prime)