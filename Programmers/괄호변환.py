from collections import deque

def solution(p):
    return make_right(p)

def split_uv(string):
    u = ""
    for i in range(len(string)):
        u += string[i]
        if is_balanced(u):       
            if len(u) == len(string):
                v = ""
            else:
                v = string[i+1:]
            return (u, v)

def is_balanced(string):
    l = list(string)
    return l.count("(") == l.count(")")

def is_right(string):
    stack = deque()
    for s in string:
        if s == "(":
            stack.append(s)
        else:
            if len(stack) <= 0:
                continue
            stack.pop()
    return (len(stack) == 0)

def process_u(string):
    u = ""
    for i in range(1, len(string) - 1):
        if string[i] == "(":
            u += ")"
        else:
            u += "("
    return u

def make_right(string):
    if string == "":
        return string
    u, v = split_uv(string)
    if is_right(u):
        data = make_right(v)
        return (u + data)
    else:
        data = "("
        data += make_right(v)
        data += ")"
        data += process_u(u)
        return data