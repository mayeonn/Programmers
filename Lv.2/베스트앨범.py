# 해시
# eg. 
# genres    ["classic", "pop", "classic", "classic", "pop"]
# plays     [500, 600, 150, 800, 2500]
# return    [4, 1, 3, 0]
def solution(genres, plays):
    answer = []
    genres_play_dict = {}
    genres_idx_dict = {}
    
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre in genres_play_dict:
            genres_play_dict[genre] += play
            genres_idx_dict[genre].append(idx)
        else:
            genres_play_dict[genre] = play
            genres_idx_dict[genre] = [idx]

    ordered_genres = [x[0] for x in sorted(genres_play_dict.items(), key = lambda x: x[1], reverse = True)]
    
    for genre in ordered_genres:
        genres_idx_dict[genre].sort(key = lambda x: (plays[x], -x), reverse = True)
        for a in genres_idx_dict[genre][:2]:
            answer.append(a)
    
    return answer