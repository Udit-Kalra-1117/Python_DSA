def prevGreater(a):
    stack = []
    list = []

    stack.append(a[len(a) - 1])
    list.append("-")

    for i in range(len(a)-2, -1, -1):
        while len(stack) > 0 and stack[-1] <= a[i]:
            stack.pop()

        if len(stack) == 0:
            list.append("-")
        else:
            list.append(stack[-1])

        stack.append(a[i])

    list.reverse()
    print(" ".join(str(x) for x in list))


array = [30, 50, 20, 15, 25]
print()
prevGreater(array)
print()