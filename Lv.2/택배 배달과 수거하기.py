def solution(cap, n, deliveries, pickups):
    result = 0
    stackD = [idx+1 for idx, x in enumerate(deliveries) for _ in range(x)]
    stackP = [idx+1 for idx, x in enumerate(pickups) for _ in range(x)]

    while stackD or stackP:
        box = []
        for _ in range(cap):
            if stackD:
                box.append(stackD.pop())
            if stackP:
                box.append(stackP.pop())
        result += max(box)*2
    print(result)
    return result