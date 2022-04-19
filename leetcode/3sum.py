

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                for k, z in enumerate(nums):
                    if i != j and i !=k and j != k \
                        and nums[i] + nums[j] + nums[k] == 0:
                        print(i, j, k)
                        answer.add((nums[i], nums[j], nums[k]))
        return answer

nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))