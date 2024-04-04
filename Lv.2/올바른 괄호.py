# Stack
def solution(s):
    stack = []
    current = ""
    for a in s:
        if not stack:
            stack.append(a)
            current = a
        elif (current=="(" and a==")"):
            current = stack.pop()
        else:
            stack.append(a)

    return len(stack)==0