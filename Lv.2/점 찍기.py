def solution(k, d):
    answer = 0
    
    for x in range(0, d+1, k):
        # 2중 for 문 사용하지 않기 위해 모든 점에 대한 길이를 구하는 것이 아니라
        # 각 x에 대한 y의 최댓값을 구함
        maxY = (d**2-x**2) **0.5
        y = int(maxY//k)+1
        answer+=y
    return answer

print(solution(2, 4))
