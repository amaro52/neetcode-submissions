class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0] if nums else -1

        result = [0] * len(nums)
        result[0] = nums[0]
        result[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            new_money = result[i - 2] + nums[i]
            result[i] = max(result[i - 1], new_money)

        return result[-1]