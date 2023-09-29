def solution(today, terms, privacies):
    answer = []

    def stringToArr(date):
        return list(map(int, date.split('.')))
    def arrToString(date):
        return "%04d.%02d.%02d"%(date[0], date[1], date[2])

    termsDict = dict()
    for x in terms:
        a, b = x.split()
        termsDict[a] = int(b)
    for idx, x in enumerate(privacies):
        a, b = x.split()
        date = stringToArr(a)

        date[1] += termsDict[b]
        date[2] -= 1

        date[1] += date[2]//28
        date[2] %= 28

        date[0] += date[1]//12
        date[1] %= 12

        if date[2]==0:
            date[2] += 28
            date[1] -= 1     
        if date[1]==0:
            date[1] += 12
            date[0] -= 1

        newDate = arrToString(date)
        if newDate < today:
            answer.append(idx+1)

    return answer

solution("2019.12.09", ["A 12"], ["2018.12.10 A", "2010.10.10 A"])