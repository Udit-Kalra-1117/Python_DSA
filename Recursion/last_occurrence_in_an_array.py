def last_occurrence(arr, size, i, value, position):
    if i == size:
        return position  # Return the last position found, which might be -1 if not found.
    if arr[i] == value:
        position = i  # Update the position only if the element is found.
    return last_occurrence(arr, size, i+1, value, position)

array = []
elements = int(input("Enter the number of elements of the array: "))
print("Enter the elements of the array on a new line each: ")
for i in range(elements):
    element = int(input())
    array.append(element)
v = int(input("Enter the required element to be searched from the given array: "))
index = last_occurrence(array, len(array), 0, v, -1)  # Start the position with -1
if index == -1:
    print("The element is not found in the given array")
else:
    print("The last occurring index of", v, "is:", index)
