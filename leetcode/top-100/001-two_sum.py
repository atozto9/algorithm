from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # exactly one solution

        # brute force
        def _brute_force():
            for i, x in enumerate(nums):
                for j, y in enumerate(nums[i + 1:]):
                    if x + y == target:
                        return i, j + i + 1

        # Two-pass hash table
        hash_table = {x: i for i, x in enumerate(nums)}
        for i, x in enumerate(nums):
            v = target - x
            if v in hash_table and hash_table[v] != i:
                return i, hash_table[v]

        # TODO: One-pass hash table


if __name__ == '__main__':
    solution = Solution()

    result = solution.twoSum([2, 7, 11, 15], 9)
    print(result)