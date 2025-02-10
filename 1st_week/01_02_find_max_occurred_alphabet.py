def find_max_occurred_alphabet(string):
    string = string.replace(" ", "")
    array = [0] * 26
    for char in string:
        array[ord(char) - ord("a")] += 1

    max_occurred = array[0]
    max_occurred_alphabet = "a"

    for  i in range(0, 26):
        if array[i] > max_occurred:
            max_occurred = array[i]
            max_occurred_alphabet = chr(i + ord("a"))

    return max_occurred, max_occurred_alphabet


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))