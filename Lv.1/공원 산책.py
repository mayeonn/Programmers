def solution(park, routes):
    arrPark = []
    arrRoutes = []
    for x in park:
        arrPark.append(list(x))
    for x in routes:
        arrRoutes.append(x.split())
    
    w = len(arrPark[0])
    h = len(park)
    location = []
    for i in range(h):
        for j in range(w):
            if arrPark[i][j]=='S':
                location.append(i)
                location.append(j)
                break

    def makeCheckList(way, n):
        checkList = []
        if way=='E':
            checkList = [[location[0], location[1]+i] for i in range(1,n+1)]
        elif way=='W':
            checkList = [[location[0], location[1]-i] for i in range(1,n+1)]
        elif way=='S':
            checkList = [[location[0]+i, location[1]] for i in range(1,n+1)]
        else:
            checkList = [[location[0]-i, location[1]] for i in range(1,n+1)]
        return checkList
    
    def check(checkList):
        for [x, y] in checkList:
            if x<0 or y<0 or x>h-1 or y>w-1:
                return False
            elif arrPark[x][y]=='X':
                return False
        return True


    for cmd in arrRoutes:
        checkList = makeCheckList(cmd[0], int(cmd[1]))
        if check(checkList):
            location = checkList[-1]
  
    return location