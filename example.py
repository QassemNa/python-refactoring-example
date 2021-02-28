def calculate_print(a,b):
    sum = a+b
    multi = a*b
    return sum, multi

def printing(sum, multi):
    print('Sum is', sum)
    print('Multi is', multi)

sum, multi = calculate_print(1,2)
printing(sum, multi)