# Day 19 코드가 너무 지저분해서 수정
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        for log in logs:
            if log.split()[1].isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)
        letter_logs.sort(key = lambda x : (x.split()[1:], x.split()[0]))
        return letter_logs + digit_logs