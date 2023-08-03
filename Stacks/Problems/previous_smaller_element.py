def previous_smaller(arr):
    stack = []
    ans = []
    for i in arr:
        if stack and stack[-1] > i:
            while stack:
                if stack[-1] > i:
                    stack.pop()
                else:
                    break
        if stack:
            ans.append(stack[-1])
            stack.append(i)
        else:
            ans.append(-1)
            stack.append(i)
    return ans

arr = [1,3,2]
print(previous_smaller(arr))
print()