def calculate_print0(a,b):
    sum = a+b
    multi = a*b
    return sum, multi

def printing0(sum, multi):
    print('Sum is', sum)
    print('Multi is', multi)

sum, multi = calculate_print0(1,2)
printing0(sum, multi)
