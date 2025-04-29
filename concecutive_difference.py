def max_consecutive_difference(lst):
    
    if len(lst)<2:
        return 0
    max_diff=0
    for i in range(1,len(lst)):
        x=abs(lst[i]-lst[i-1])
        if x>max_diff:
            max_diff=x
    return max_diff        
lst = list(map(int, input("Enter the numbers: ").split()))

print( max_consecutive_difference(lst))