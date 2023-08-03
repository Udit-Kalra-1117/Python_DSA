def nextGreater(a):
    for i in range(len(a)):
        flag = False
        for j in range(i + 1, len(a)):
            if a[j] > a[i]:
                print(a[j], end=" ")
                flag = True
                break
        if not flag:
            print("-", end=" ")

array = [30, 50, 20, 15, 25]
print()
nextGreater(array)
print()