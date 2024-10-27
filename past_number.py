
def del_not_p_number(list_number,number_p,n):
    if number_p == 5:
        return del_not_p_number(list_number,list_number[list_number.index(number_p)+1],n)
    if number_p>(n**(0.5)):
        a = list_number
        return len(list_number)
    
    for number in list_number[:]:
        if number*number_p in list_number:
            list_number.remove(number*number_p)
        if number*number_p> n:
            break
    return del_not_p_number(list_number,list_number[list_number.index(number_p)+1],n)

def search_count_numbers(n):
    if n<2:
        return 0
    elif n<3:
        return 1
    list_number = [2, 3]
    for i in range(9, n+1, 2):
        if i%10 != 5:
            list_number.append(i)
    return del_not_p_number(list_number,3,n)

print(search_count_numbers(1))

