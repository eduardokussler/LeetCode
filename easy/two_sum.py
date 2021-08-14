class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      first_index = 0
      second_index = 1
      for j in range(0, len(nums) - 1):
        first_index = j
        for i in range(first_index+1, len(nums)):
          second_index = i
          if nums[first_index] + nums[second_index] == target:
            return first_index, second_index
          