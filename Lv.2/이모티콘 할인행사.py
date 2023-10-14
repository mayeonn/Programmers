from itertools import product

def solution(users, emoticons):
    answer = [0, 0]

    # 모든 할인율 조합
    discount = product([10,20,30,40], repeat=len(emoticons))

    # 각 할인율 조합마다 가입자와 판매액 구하기
    for percent in discount:
        numofRegister = 0   #가입자수
        sumofPrice = 0      #총판매액
        
        # 할인율조합마다 - 유저마다
        for user in users:
            userPaid = 0

            # 할인율조합마다 - 유저마다 - 이모티콘마다 살건지
            for idx, sale in enumerate(percent):
                price = emoticons[idx] * (100 - sale) // 100
                if sale > user[0]:
                    userPaid += price
            
            if userPaid >= user[1]:
                numofRegister += 1
            else:
                sumofPrice += userPaid
        # 해당 조합이 max인지 확인
        if answer[0] < numofRegister:
            answer = [numofRegister, sumofPrice]
        elif answer[0]==numofRegister and answer[1]<sumofPrice:
            answer[1] = sumofPrice
    
        print(answer)
    return answer
