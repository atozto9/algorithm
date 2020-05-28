class Solution:
    def __init__(self):
        self._int_min = -2**31
        self._int_max = 2**31 - 1

    def reverse(self, x: int) -> int:

        reversed_x = int(str(abs(x))[::-1])

        if x < 0:
            reversed_x *= -1

        if self._int_min > reversed_x or self._int_max < reversed_x:
            return 0

        return reversed_x

