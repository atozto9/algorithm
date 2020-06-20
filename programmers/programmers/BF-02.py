from itertools import permutations


def solution(numbers):
    def _is_prime(x):
        if x <= 1:
            return False
        else:
            for i in range(2, x):
                if x % i == 0:
                    return False
        return True

    answer = 0

    check_list = []
    for i in range(1, len(numbers) + 2):
        check_list += [int(''.join(x)) for x in permutations(numbers, i)]
    check_list = set(check_list)

    for x in check_list:
        answer += _is_prime(x)

    return answer