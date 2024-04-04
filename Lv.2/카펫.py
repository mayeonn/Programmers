# 완전탐색
# eg.
# brown 10 yellow 2 -> return [4, 3]
# brown 24 yellow 24 -> return [8, 6]
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    
    for h in range(3, int(total)):
        if total%h == 0:
            w = int(total/h)
            if (h-2)*(w-2) == yellow:
                answer = [w, h]
                answer.sort(reverse=True)
                return answer

    