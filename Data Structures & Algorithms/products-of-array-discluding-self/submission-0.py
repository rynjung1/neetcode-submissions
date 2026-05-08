class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left = []
        right = []
        cur_left = 1
        cur_right = 1

        for index, num in enumerate(nums): 
            left.append(cur_left)
            cur_left *= num
        
        for i in range(len(nums) - 1, -1, -1):
            right.append(cur_right)
            cur_right *= nums[i]

        for i in range(len(nums)):
            output.append(left[i] * right[len(nums) - i - 1])

        return output