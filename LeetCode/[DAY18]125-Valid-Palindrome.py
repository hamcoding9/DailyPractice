# What I submitted
def isPalindrome(self, s: str) -> bool:
    s = ''.join([l for l in s.lower() if l.isalpha() or l.isdigit()])
    return s == s[::-1]

# Another Version(using regex)
import re
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    s = re.sub('[^0-9a-zA-Z]','',s)
    return s == s[::-1]
