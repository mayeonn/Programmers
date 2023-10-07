import math
def solution(w,h):
    answer = w*h
    answer -= (w + h - math.gcd(w,h))
    # 최대공약수
    return answer