def previous_greater_element(a):
    stack = []
    stack.append(a[0])
    print("-", end=" ")

    for i in range(1, len(a)):
        while len(stack) > 0 and stack[-1] <= a[i]:
            stack.pop()

        if len(stack) == 0:
            print("-", end=" ")
        else:
            print(stack[-1], end=" ")

        stack.append(a[i])

array = [30, 50, 20, 15, 25]
previous_greater_element(array)
print()
