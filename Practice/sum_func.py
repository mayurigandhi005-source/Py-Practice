def sum_even(*args):
    total = 0
    for i in args:
        if i %2==0:
            total=total+i
    return total
print(sum_even(1,2,3,4,5,6,7,8,9))    

