def gen_num(limit):
    n=1
    while n<=limit:
        yield n
        n+=1
for num in gen_num(3):
    print(num)        
    