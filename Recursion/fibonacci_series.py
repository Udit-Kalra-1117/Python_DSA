def fibonacci_series(n):
    if n <= 1 :
        return n
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)
    
number = int(input("Enter the number of elements to find the fibonacci series sum for: "))
if number <= 0:
    print("Please enter a positive number!!")
else:
    print("Fibonacci series:", end=" ")
    for i in range(number):
        print(fibonacci_series(i), end=" ")
    print("\nThe sum of",number,"elements in the fibonacci series is:",fibonacci_series(number))