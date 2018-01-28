class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        q = 0
        for i in range(0, len(nums)):
            m = target - nums[i]
            if m in nums:
                q = nums.index(m)
                if q != i:
                    break
        return [i, q]
