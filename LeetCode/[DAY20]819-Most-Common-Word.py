import collections, re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[^a-z ]', ' ', paragraph.lower())
        rank = collections.Counter(paragraph.split())
        return [word for word, count in rank.most_common() if word not in banned][0]
    
# 책에서 제시한 정답
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[\w]', ' ', paragraph)
             .lower().split()
             if word not in banned]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]