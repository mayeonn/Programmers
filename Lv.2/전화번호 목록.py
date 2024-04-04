# 해시
def solution(phone_book):
    answer = True
    phone_book.sort()   # 같은 접두사를 가진다면 바로 뒤에 오게 됨 -> 바로 뒤에 것만 탐색
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            answer = False
            break
    
    return answer