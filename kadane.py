def kadane(t):
    t=[-2,1,3,4,-1,-5,4]
    sum_max=0
    sum=0
    for i in t:
        if sum<0:
            sum=0
        if sum>sum_max:
            sum_max=sum
            return sum_max


