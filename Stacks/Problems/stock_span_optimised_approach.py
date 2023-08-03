def stockSpan(a):
    stack = []
    stack.append(0)
    print(1, end=" ")

    for i in range(1, len(a)):
        while len(stack) != 0 and a[stack[-1]] <= a[i]:
            stack.pop()
        if len(stack) == 0:
            print(i + 1, end=" ")
        else:
            print(i - stack[-1], end=" ")
        stack.append(i)


# Driver code
array = [100, 20, 30, 60, 38, 36, 32, 55, 80, 50, 120]
stockSpan(array)
print()