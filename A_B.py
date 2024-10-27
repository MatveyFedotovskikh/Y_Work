def maxsize_number_a(a,b):
    b = sorted(b,reverse=True)
    number_is_B = 0
    for number_is_A in range(len(a)):
        if int(a[number_is_A]) < int(b[number_is_B]):
            a =  f'{a[:number_is_A]}{b[number_is_B]}{a[number_is_A+1:]}'
            number_is_B += 1
            if number_is_B == len(b):
                return a
    return a 

a = '43509'
b = '32907'
print(maxsize_number_a(a,b))