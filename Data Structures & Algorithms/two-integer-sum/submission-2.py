class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        res = []
        for i in range(len(nums)):
            if nums[i] in dic:
                res = [dic[nums[i]],i]
            dic[target-nums[i]]=i
        return res