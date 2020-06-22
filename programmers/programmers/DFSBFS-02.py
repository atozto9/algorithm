def solution(n, computers):
    answer = 0

    visited = [False] * n

    while False in visited:
        stacks = [visited.index(0)]

        while stacks:
            stack = stacks.pop()

            for i in range(n):
                if not visited[i] and computers[stack][i]:
                    visited[i] = True
                    stacks.append(i)
        answer += 1

    return answer