def solution(wallpaper):    
    fileLocationX, fileLocationY = [], []
    for x, row in enumerate(wallpaper):
        for y, char in enumerate(row):
            if char=='#':
                fileLocationX.append(x)
                fileLocationY.append(y)

    return [min(fileLocationX), min(fileLocationY), max(fileLocationX)+1, max(fileLocationY)+1]