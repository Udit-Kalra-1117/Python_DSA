def maxArea(a):
    result = 0

    for i in range(len(a)):
        count=1
        for j in range(i-1,-1,-1):
            if a[j]>=a[i]:
                count+=1
            else:
                break
        for j in range(i+1, len(a)):
            if a[j]>=a[i]:
                count+=1
            else:
                break
        temp = count * a[i]
        result = max(result, temp)
    return result

array = [12, 3, 4, 4, 1, 5, 7]
print()
print("Max Area is: " + str(maxArea(array)))
print