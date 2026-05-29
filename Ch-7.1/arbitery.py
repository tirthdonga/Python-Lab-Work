def arbi_num(*args):
    if not args:
        return 0, 0
    
    total_sum = sum(args)
    total_product = 1
    
    for num in args:
        total_product *= num
        
    return total_sum, total_product

print(arbi_num(2, 3, 4))