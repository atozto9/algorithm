def solution(numbers, target):
    def _dfs(numbers, target, current_v):
        if not numbers:
            if current_v == target:
                return 1
            else:
                return 0

        return _dfs(numbers[1:], target, current_v + numbers[0]) + \
               _dfs(numbers[1:], target, current_v - numbers[0])

    # answer = _dfs(numbers, target, 0)

    f_list = [0]
    for n in numbers:
        # f_list = sum([[x+n, x-n] for x in f_list], [])
        f_list = [a for x in f_list for a in [x + n, x - n]]
    answer = f_list.count(target)

    return answer