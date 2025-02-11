input = 20


def find_prime_list_under_number(number):
    return_arr = []
    for i in range(2, number):
        is_prime = True
        for j in range(1, i):
            if j != 1 and j != i:
                if i%j == 0:
                    is_prime = False
                    break
        if is_prime: return_arr.append(i)
    return return_arr


result = find_prime_list_under_number(20)
print(result)