class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        counter1 = 0
        for i in range (0, len(nums)):
            if nums[i] != 0:
                nums[counter1] = nums[i]
                counter1 = counter1 + 1
        for i in range (counter1, len(nums)):
            nums[i] = 0


        
        """
        Do not return anything, modify nums in-place instead.
        """

        