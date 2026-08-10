class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n

        result = [0] * n
        result[0] = 1
        result[1] = 2

        for i in range(2, n):
            result[i] = result[i - 2] + result[i - 1]

        return result[-1]