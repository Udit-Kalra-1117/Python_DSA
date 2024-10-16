# Quick sort in Python

# function to find the partition position
def partition(array, low, high):
    # choose the leftmost element as pivot
    pivot = array[low]

    # pointer for element at next consecutive position from pivot
    i = low + 1

    # pointer for the rightmost element
    j = high

    # traverse through all elements
    # compare each element with pivot
    while True:
        
        # this loop runs from left-to-right and finds the element which is greater than pivot
        # so that all elements greater than pivot can be shifted to the right of pivot
        while i <= j and array[i] <= pivot:
            i += 1

        # this loop runs from right-to-left and finds the element which is smaller than pivot
        # so that the elements smaller than pivot can be shifted to the left of pivot
        while i <= j and array[j] >= pivot:
            j += 1

        # this helps in placing the values of the array in sorted order
        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            break
            
    # swap the pivot element with the smaller element (in value when compared by pivot) specified by j
    (array[low], array[j]) = (array[j], array[low])

    # return the position from where partition is done
    return j

# function to perform quicksort
def quickSort(array, low, high):
    if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("\nArray before applying quick sort: {}".format(data))
quickSort(data, 0, len(data) - 1)
print('\nSorted Array after applying quick sort: {}'.format(data))
