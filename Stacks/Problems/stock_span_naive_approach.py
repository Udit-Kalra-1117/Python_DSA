def stock_span(a):
    for i in range(len(a)):
        count_current_span = 1
        for j in range(i-1,-1,-1):
            if a[j]<=a[i]:
                count_current_span+=1
        print("{} : {}".format(a[i],count_current_span))

array = [12, 14, 15, 7, 15, 17, 5]
stock_span(array)