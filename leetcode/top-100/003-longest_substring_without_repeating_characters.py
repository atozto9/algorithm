class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        def _brute_force():
            # time limit exceeded
            if s is '':
                return 0

            substring_dict = {}

            for i in range(len(s)):
                for j in range(1, len(s)):
                    if len(s[i:j]) >= 1:
                        if s[j] in s[i:j]:
                            break

                        substring_dict[s[i:j+1]] = len(s[i:j+1])

            if not bool(substring_dict):
                return 1

            return max(substring_dict.values())

        substring_dict = {}

        if len(s) > 0:
            substring_dict[s[0]] = 1
        elif len(s) == 0:
            return 0

        start_i, end_i = 0, 1
        while end_i < len(s):

            if s[end_i] in s[start_i:end_i]:
                start_i = s[start_i:end_i].index(s[end_i]) + start_i + 1
                end_i += 1
                continue
            else:
                end_i += 1

            substring_dict[s[start_i:end_i]] = len(s[start_i: end_i])

        return max(substring_dict.values())


if __name__ == '__main__':
    solution = Solution()

    result = solution.lengthOfLongestSubstring("bbtablud")
    print(result)