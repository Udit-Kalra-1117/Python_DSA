def tribonacci_series(n):
    if n <= 2 :
        return n
    else:
        return tribonacci_series(n-1) + tribonacci_series(n-2) + tribonacci_series(n-3)
    
number = int(input("Enter the number of elements to find the tribonacci series sum for: "))
if number <= 0:
    print("Please enter a positive number!!")
else:
    print("Tribonacci series:", end=" ")
    for i in range(number):
        print(tribonacci_series(i), end=" ")
    print("\nThe sum of",number,"elements in the tribonacci series is:",tribonacci_series(number))