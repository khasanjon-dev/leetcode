def score_of_string(s: str) -> int:
    result = 0
    for i in range(1, len(s)):
        result += abs(ord(s[i - 1]) - ord(s[i]))
    return result


print(score_of_string('zaz'))
