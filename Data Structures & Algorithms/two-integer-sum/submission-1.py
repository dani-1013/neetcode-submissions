class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        for i, arr in enumerate(nums):
            j = target - arr

            if j in num_to_index:
                return[num_to_index[j], i]

            num_to_index[arr] = i