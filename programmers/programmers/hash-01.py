def solution(participant, completion):
    def _hash_sol(par, com):
        hash_to_name = {}
        hash_sum = 0
        for p in par:
            hash_v = hash(p)
            hash_to_name[hash_v] = p
            hash_sum += hash_v
        for c in com:
            hash_v = hash(c)
            hash_to_name[hash_v] = c
            hash_sum -= hash_v

        return hash_to_name[hash_sum]

    participant = sorted(participant)
    completion = sorted(completion)

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]