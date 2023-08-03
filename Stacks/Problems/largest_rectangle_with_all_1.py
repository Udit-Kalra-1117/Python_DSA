def largestHistRow(a):
    result = []
    top_val = 0
    max_area = 0
    area = 0
    i = 0

    while(i<len(a)):
        if (len(result)==0) or (a[result[-1]]<a[i]):
            result.append(i)
            i+=1
        else:
            top_val = a[result.pop()]
            area = top_val * i
            if len(result):
                area = top_val * (i - result[-1] - 1)
            max_area = max(area, max_area)

    while len(result):
        top_val = a[result.pop()]
        area = top_val * i
        if len(result):
            area = top_val * (i-result[-1]-1)
        max_area = max(area, max_area)
    return max_area

def maxRectangle(a):
    result = largestHistRow(a[0])

    for i in range(1, len(a)):
        for j in range(len(a[i])):
            if a[i][j]:
                a[i][j] += a[i-1][j]
        result = max(result, largestHistRow(a[i]))
    return result

array = [[0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0]]
print()
print("Maximum rectangle is: ", maxRectangle(array))


# # A basic code for matrix input from user

# R = int(input("Enter the number of rows:"))
# C = int(input("Enter the number of columns:"))

# # Initialize matrix
# matrix = []
# print("Enter the entries row-wise:")

# # For user input
# for i in range(R):		 # A for loop for row entries
# 	a =[]
# 	for j in range(C):	 # A for loop for column entries
# 		a.append(int(input()))
# 	matrix.append(a)

# # For printing the matrix
# for i in range(R):
# 	for j in range(C):
# 		print(matrix[i][j], end = " ")
# 	print()
