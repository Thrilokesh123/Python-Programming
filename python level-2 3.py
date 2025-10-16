n=6
s=sum(i for i in range(1,n) if n%i==0)
print("it is a perfect number" if s==n else "not a perfect number")
