def next_smaller(arr):
    stack = []
    ans = []
    for i in reversed(arr):
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
    return ans[::-1]

arr = [1,3,2]
print(next_smaller(arr))
print()