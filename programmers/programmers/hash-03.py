from collections import Counter


def solution(clothes):
    answer = 1

    num_items_each_cat = Counter([cat for item, cat in clothes]).values()

    for x in num_items_each_cat:
        answer *= (x + 1)

    answer -= 1

    return answer