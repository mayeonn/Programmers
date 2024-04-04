# Stack/Queue
# eg.
# arr   [1,1,3,3,0,1,1]
# answer [1,3,0,1]
def solution(arr):
    answer = []
    
    for num in arr:
        if len(answer)==0:
            answer.append(num)
        elif answer[len(answer)-1] != num:
            answer.append(num)
        
    
    return answer