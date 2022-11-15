def is_palindrome(s):
    return s == s[::-1]

def solution(s):
    for size in range(len(s), 0, -1):
        for index in range(0, len(s) - size + 1):
            substring = s[index:index+size]
            if is_palindrome(substring):
                return len(substring)