def insertion_sort(a):
    for i in range(1,len(a)):
        temp = a[i]
        j = i - 1
        while j>=0 and temp<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=temp


array = [10,90,60,20,50,1000,500,30,40]
print("Array before applying insertion sort: {}".format(array))
insertion_sort(array)
print("Array after applying insertion sort: {}".format(array))
