class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashResult = {}

        for x in range(len(nums)):
            if target-nums[x] in hashResult:
                return [hashResult[target-nums[x]],x]
            hashResult[nums[x]] = x

        return []