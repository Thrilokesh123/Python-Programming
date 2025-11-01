def removeKdigits(num, k):
    stack = []
    for d in num:
        while k and stack and stack[-1] > d:
            stack.pop()
            k -= 1
        stack.append(d)
    stack = stack[:-k] if k else stack
    result = ''.join(stack).lstrip('0')
    return result if result else "0"
print(removeKdigits("1432219", 3))  
print(removeKdigits("10200388", 1))  
