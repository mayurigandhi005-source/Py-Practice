def find_max(*args):
    if len(args) == 0:
        return 0 
    return max(args)
print(find_max(10,25,9))
print(find_max())