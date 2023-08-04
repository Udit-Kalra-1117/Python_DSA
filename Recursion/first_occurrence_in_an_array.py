def first_occurrence(arr, size, i, value):
    if i == size:
        print(value,"is not present in the given array")
        return
    if arr[i] == value:
        print("First occurrence of",value,"is at index:",i)
        return
    first_occurrence(arr, size, i+1, value)

array = []
elements = int(input("Enter the number of elements of the array: "))
print("Enter the elements of the array on a new line each: ")
for i in range(elements):
    element=int(input())
    array.append(element)
v = int(input("Enter the required element to be searched from the given array: "))
first_occurrence(array, len(array), 0, v)