def binarySearch(a, i, l, h):
    # Repeat until the pointers low and high meet each other
    while l <= h:
        m = l + (h - l)//2
        if a[m] == i:
            return m
        elif a[m] < i:
            l = m + 1
        else:
            h = m - 1
    return -1


array = [3, 4, 5, 6, 7, 8, 9]
item = int(input("Enter the element to be searched: "))

result = binarySearch(array, item, 0, len(array)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")