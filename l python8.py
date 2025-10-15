data = [12, 45, 83, 52]
mean = sum(data) / len(data)
data.sort()
n = len(data)
if n % 2 == 0:
    median = (data[n//2 - 1] + data[n//2]) / 2
else:
    median = data[n//2]
mode = None
for i in data:
    if data.count(i) > 1:
        mode = i
        break
if mode is None:
    mode = data[0]  
average = (mean + median + mode) / 3
print("Output:", int(average))
