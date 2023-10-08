def isCorrect(s):
    length = len(s)//2
    for _ in range(length):
        s = s.replace("[]", "")
        s = s.replace("()", "")
        s = s.replace("{}", "")
        if len(s)==0:
            return True
    return False

def left(s):
    return s[1:] + s[0]

def solution(s):
    answer = 0
    for _ in s:
        if isCorrect(s):
            answer+=1
        s = left(s)
    return answer