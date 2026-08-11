from collections import defaultdict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        INTEGERS = [0, 1, 2]

        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1

        i = 0
        for n in INTEGERS:
            freq = freqs[n]
            for _ in range(freq, 0, -1):
                nums[i] = n
                i += 1

        print(nums)

