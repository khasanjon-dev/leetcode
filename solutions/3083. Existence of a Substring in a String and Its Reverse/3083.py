def is_substring_present(s: str) -> bool:
    for i in range(len(s) -1):
        if s[i: i + 2] in s[::-1]:
            return True
    return False


print(is_substring_present('leetcode'))
