class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in range (len(nums)):
            amount = 0
            for j in nums:
                if j<nums[i]:
                    amount+=1
            res.append(amount)
        return res
