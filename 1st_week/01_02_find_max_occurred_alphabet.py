def find_max_occurred_alphabet(string):
    string = string.replace(" ", "")
    array = [0] * 26
    for char in string:
        array[ord(char) - ord("a")] += 1

    max_occurred = array[0]
    for num in array:
        if num > max_occurred:
            max_occurred = num
    return max_occurred


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))