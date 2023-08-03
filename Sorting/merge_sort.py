def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two sub-arrays
        r = len(array)//2
        L = array[:r]
        R = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1


array = [6, 5, 12, 10, 9, 1]
print("\nArray before applying merge sort is: {}".format(array))
mergeSort(array)
print("\nSorted array after applying merge sort is: {}".format(array))