# cycle in itertools

def solution(answers):
    answer = [0, 0, 0]
    pattens = [[1, 2, 3, 4, 5],
               [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i, ans in enumerate(answers):
        for j in range(len(pattens)):
            answer[j] += (pattens[j][i%len(pattens[j])] == ans)

    max_v = max(answer)

    answer = [i+1 for i, x in enumerate(answer) if x == max_v]
    return answer
