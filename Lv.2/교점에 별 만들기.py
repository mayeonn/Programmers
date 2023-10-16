from itertools import combinations

def findMeet(line1, line2):
    A, B, E = line1
    C, D, F = line2
    '''
    Ax + By + E = 0
    Cx + Dy + F = 0

    x = (BF - ED) / (AD - BC)
    y = (EC - AF) / (AD - BC)

    위 식은 정리, 대입해서 구할 수 있음
    '''

    #  AD - BC = 0 (분모가 0인 경우 평행 또는 일치)
    if A*D == B*E:
        return
    
    x = (B*F - E*D) / (A*D - B*C)
    y = (E*C - A*F) / (A*D - B*C)

    if int(x)==x and int(y)==y:
        return [int(x), int(y)]


def solution(line):
    meets = []

    for line1, line2 in combinations(line, 2):
        meet = findMeet(line1, line2)
        if meet:
            meets.append(meet)

    minX = min([x[0] for x in meets])
    maxX = max([x[0] for x in meets])
    minY = min([x[1] for x in meets])
    maxY = max([x[1] for x in meets])

    answer = [['.']*(maxX-minX + 1) for _ in range(maxY-minY + 1)]

    for x, y in meets:
        answer[y-minY][x-minX] = '*'
    
    answer.reverse()
    return [''.join(a) for a in answer]

print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))