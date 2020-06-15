def solution(phone_book):
    def _hash_sol(phone_book):
        answer = True

        hash_map = {}

        for p_n in phone_book:
            hash_map[p_n] = [1]

        for p_n in phone_book:
            c_seq = ""

            for c in p_n:
                c_seq += c
                if c_seq in hash_map and c_seq != p_n:
                    return False

        return answer

    answer = True

    phone_book.sort(key=len)

    for i, p_1 in enumerate(phone_book[:-1]):
        # if any([p_2.startswith(p_1) for p_2 in phone_book[i+1:]]):
        #    return False
        for p_2 in phone_book[i + 1:]:
            if p_2.startswith(p_1):
                return False

    return answer