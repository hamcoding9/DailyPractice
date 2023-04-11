from collections import deque
def solution(s):
    element, queue = [], [] 
    example, digit = list(s), ""
    for i in range(1, len(s)-1):
        if s[i] == "}":
            queue.append(element)
            element = []
            continue
        if s[i].isdigit():
            digit += s[i]
        if s[i].isdigit() and s[i+1] in [",", "}"]:
            element.append(int(digit))
            digit = ""
    queue = deque(sorted(queue, key=lambda x:len(x)))
    result = []
    result.append(queue.popleft()[0])
    while queue:
        element = queue.popleft()
        for e in element:
            if e in result:
                continue
            else:
                result.append(e)
    return result