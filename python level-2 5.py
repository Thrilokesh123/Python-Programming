a=[14,16,87,36,25,89,34]
M,N=1,3
a.sort()
print(f"{M}st Maximum Number={a[-M]}")
print(f"{N}rd Minimum Number={a[N-1]}")
print("Sum=",a[-M]+a[N-1])
print("Difference=",a[-M]-a[N-1])
