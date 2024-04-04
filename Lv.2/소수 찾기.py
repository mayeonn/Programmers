# 완전탐색
from itertools import permutations
import math

def solution(numbers):
    possibleNums = set()
    for i in range(len(numbers)):        
        for arr in list(permutations(numbers, i+1)):
            possibleNums.add(int("".join(arr)))
    
    answer = list(filter(lambda x: is_prime_number(x), possibleNums))
    return len(answer)

# 소수 찾는 함수. 암기하기
def is_prime_number(x):
    if x==0 or x==1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x%i==0:
            return False
    return True