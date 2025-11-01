n = input()
if len(n)%2==0:
    a, b = int(n[:len(n)//2]), int(n[len(n)//2:])
    print((a+b)**2 == int(n))
else:
    print(False)