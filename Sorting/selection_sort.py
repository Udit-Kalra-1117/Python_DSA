def selection_sort(a):
    for i in range(len(a)-1):
        min_index=i
        for j in range(i+1, len(a)):
            if a[min_index]>a[j]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

array = [10,90,60,20,50,1000,500,30,40]
print("Array before applying selection sort: {}".format(array))
selection_sort(array)
print("Array after applying selection sort: {}".format(array))