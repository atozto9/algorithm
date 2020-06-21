def solution(budgets, M):
    answer = 0
    minimum, maximum = 0, max(budgets)

    while minimum <= maximum:
        mid = (maximum + minimum) // 2

        tmp = [x if x <= mid else mid for x in budgets]

        sum_of_tmp = sum(tmp)
        if sum_of_tmp > M:
            maximum = mid - 1
        else:
            answer = mid
            minimum = mid + 1

    return answer


if __name__ == '__main__':
    print(solution([50, 100, 99, 140, 120], 485))