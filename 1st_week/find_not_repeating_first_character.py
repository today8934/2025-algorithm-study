def find_not_repeating_first_character(string):
    arr = [0] * 26
    for char in string:
        arr[ord(char) - 97]+=1

    return_char = "_"
    for char in string:
        if arr[ord(char) - 97] == 1:
            return_char = char
            break
    return return_char


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 = _ 현재 풀이 값 =", result("aaaaaaaa"))