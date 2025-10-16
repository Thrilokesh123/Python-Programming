nums=[4,54,29,71,59,98,23]
p=c=0
for n in nums:
    if n>1:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:c+=1;break
        else:p+=1
print("composite numbers=",c)
print("prime numbers=",p)
