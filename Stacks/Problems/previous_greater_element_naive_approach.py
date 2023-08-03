def previous_greater_element(a):
    for i in range(len(a)):
        flag = False
        for j in range(i-1,0,-1):
            if a[j]>a[i]:
                print(a[j], end=" ")
                flag=True
                break
        if not flag:
            print("-", end=" ")
        
array = [30,50,20,15,25]
previous_greater_element(array)
print()
