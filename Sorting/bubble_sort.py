def bubble_sort(a):
    for i in range(len(a)-1):
        swapped=False
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swapped = True
        if not swapped:
            break

array = [20,50,30,10,80,60,100,90]
print("Array before applying bubble sort: {}".format(array))
bubble_sort(array)
print("Array after applying bubble sor is: {}".format(array))