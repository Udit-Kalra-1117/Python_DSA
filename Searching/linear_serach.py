def linear_search(a,l,i):
    for j in range(l):
        if a[j] == i:
            return "Element is found at index: " + str(j)
    return "Element is not present in the given array"

array = [10,20,50,30,90,40,80,70,60,200,150,400]
item=int(input("Enter the element to be searched: "))
print(linear_search(array, len(array), item))
