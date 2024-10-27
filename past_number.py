def del_not_p_number(list_number,number_p,n):
    number_p += 1
    if number_p>(n**(0.5)):
        return len(list_number)
    for number in range(2,n+1,number_p):
        if number in list_number:
            list_number.remove(number)
    return del_not_p_number(list_number,number_p,n)

def search_count_numbers(n):
    list_p_number = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]
    
    if n>list_p_number[-1]:
        list_numbers = [i for i in range(list_p_number[-1]+1,n+1)]
        
        for number_p in list_p_number:
            if number_p>(n**(0.5)):
                return len(list_p_number) + len(list_numbers)
            
            else:
                for number in range(2,n+1,number_p):
                    if number in list_numbers:
                        list_numbers.remove(number)
        if list_p_number[-1]>=(n**(0.5)):
            return len(list_p_number) + len(list_numbers)
        else:
            return del_not_p_number(list_p_number+list_numbers, number_p,n)
        
            

    else:
        i = len(list_p_number)//2
        
        while True:
            if list_p_number[i] == n or (list_p_number[i]<n and list_p_number[i+1]>n):
                return len(list_p_number[:i+1])

            elif list_p_number[i]<n:
                i+=1

            else:
                i-=1

print(search_count_numbers(13001))

