# Greedy
def solution(people, limit):
    answer = 0
    people.sort()
    # 정렬 후 양 끝쪽에서 탐색
    left = 0
    right = len(people) - 1
    
    while(left <= right):
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
    
    return answer