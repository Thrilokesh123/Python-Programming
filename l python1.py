nums = input("Enter -1 to exit, enter the numbers ").split(',')
pos = []
neg = []
for n in nums:
    num = int(n)
    if num == -1:
        break
    if num > 0:
        pos.append(num)
    elif num < 0:
        neg.append(num)
avg_pos = sum(pos) // len(pos)
avg_neg = sum(neg) // len(neg)
print("avg negative number is", avg_neg)
print("avg positive number is", avg_pos)
