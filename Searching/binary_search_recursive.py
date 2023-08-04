# Binary Search
# Binary search is very fast and efficient searching algorithm. 
# It requires to be list be in a sorted order, ie; either in ascending or descending.
# In this method, to search an element you might compare that respective element present in the center of the list 
# and if it’s same then the search is successfully finished and if not, then the list is  divided into two parts:
# one from 0th element to the centered element and other from the centered element to the last element.

# Time Complexity (Best)	Ω(1)
# Time Complexity (Avg)	Θ(log n)
# Time Complexity (Worst)	O(log n)
# Space Complexity	O(1)

def binarySearch(a, i, l, h):
    if h >= l:
        m = l + (h - l)//2
        # If found at mid, then return it
        if a[m] == i:
            return m
        # Search the left half
        elif a[m] > i:
            return binarySearch(a, i, l, m-1)
        # Search the right half
        else:
            return binarySearch(a, i, m + 1, h)
    else:
        return -1

array = [3, 4, 5, 6, 7, 8, 9]
item = int(input("Enter the element to be searched: "))
result = binarySearch(array, item, 0, len(array)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
