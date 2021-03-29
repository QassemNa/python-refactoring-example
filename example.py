def calculate_print1(a,b):
    sum = a+b
    multi = a*b
    return sum, multi

def printing1(sum, multi):
    print('Sum is', sum)
    print('Multi is', multi)

sum, multi = calculate_print1(1,2)
printing1(sum, multi)
