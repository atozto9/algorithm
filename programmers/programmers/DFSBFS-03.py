def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    visited = [False] * len(words)
    stack = [begin]

    while stack:
        x = stack.pop()
        if x == target:
            return answer

        for i, w in enumerate(words):
            if not visited[i] and len([1 for a, b in zip(x, w) if a != b]) == 1:
                visited[i] = True
                stack.append(w)

        answer += 1

    return answer