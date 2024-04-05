# Heap 힙
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)        
    
    while True:
        minimum = heapq.heappop(scoville)
        if minimum >= K:
            return answer
        elif len(scoville)<1:
            return -1
        else:
            mixed = minimum + heapq.heappop(scoville)*2
            heapq.heappush(scoville, mixed)
            answer += 1
            continue