class Solution:
    def rob(self, nums: List[int]) -> int:
        

        def house_robber1(nums_list: List[int]):
            if len(nums_list) <= 2:
                return max(nums) if nums else -1

            result = [0] * len(nums_list)
            result[0] = nums_list[0]
            result[1] = max(nums_list[0], nums_list[1])

            for i in range(2, len(nums_list)):
                new_value = result[i - 2] + nums_list[i]
                result[i] = max(result[i - 1], new_value)

            return result[-1]


        result1 = house_robber1(nums[:-1]) # everything but last element
        result2 = house_robber1(nums[1:]) # everything but first element

        return max(result1, result2)