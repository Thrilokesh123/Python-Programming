def rotate(arr, k):
    k %= len(arr)       
    return arr[-k:] + arr[:-k]

nums = [0,1,4,4,6,7]

print(rotate(nums, 4))   
print(rotate(nums, 7))   

