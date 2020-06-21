def solution(n, times):
    answer = 0

    start = 1
    end = max(times) * n

    while start <= end:
        mid = (start + end) // 2

        if sum([mid // x for x in times]) < n:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    return answer