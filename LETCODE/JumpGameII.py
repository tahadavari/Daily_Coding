

class Solution:
    def jump(self, nums: list[int]) -> int:
        step = 0
        if len(nums)==1 or nums[0]==0:
            return step
        max_index = 0
        for i in range(len(nums)-1):
            maximum = max(nums[(max_index+1):((max_index+1)+nums[max_index])])
            # print(maximum)
            step+=1
            pre_index = nums[max_index]
            max_index = nums.index(maximum)
            # print(pre_index,':p')
            
            if pre_index>=len(nums)-pre_index-i-1:
                return step
            
        


s = Solution

print(s.jump(s,[1,1,1,1]))