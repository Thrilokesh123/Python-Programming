prices = [7, 1, 5, 3, 6, 4]

buy1 = buy2 = float('inf')
profit1 = profit2 = 0

for p in prices:
    buy1 = min(buy1, p)         
    profit1 = max(profit1, p-buy1)   
    buy2 = min(buy2, p-profit1)      
    profit2 = max(profit2, p-buy2)  

print(profit2)
