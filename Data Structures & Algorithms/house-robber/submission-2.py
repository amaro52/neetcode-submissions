class Solution:
    def rob(self, nums: List[int]) -> int:
        result = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                result[i] = nums[i]
            elif i == 1:
                result[i] = max(nums[i], nums[i - 1])
            else:
                new_money = result[i - 2] + nums[i]
                result[i] = max(result[i - 1], new_money)

        return result[-1]