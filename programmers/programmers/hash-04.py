from collections import defaultdict


def solution(genres, plays):
    answer = []

    genres_dic = defaultdict(list)

    for i, (g, p) in enumerate(zip(genres, plays)):
        genres_dic[g].append((i, p))

    sorted_by_total_plays = sorted(genres_dic.items(), key=lambda x: sum([a[1] for a in x[1]]), reverse=True)

    sorted_inside = [sorted(p, key=lambda x: x[1], reverse=True) for g, p in sorted_by_total_plays]

    for p_list in sorted_inside:
        answer += [x[0] for x in p_list][:2]

    return answer