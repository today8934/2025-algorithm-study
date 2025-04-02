input = "0111110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    current_num = string[0]
    count_to_zero = 0
    count_to_one = 0

    for number in string:
        if (current_num != number):
            if (current_num == "0"): 
                count_to_one = count_to_one + 1
                current_num = "1"
            else: 
                count_to_zero = count_to_zero + 1
                current_num = "0"
            

    return min(count_to_zero, count_to_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)