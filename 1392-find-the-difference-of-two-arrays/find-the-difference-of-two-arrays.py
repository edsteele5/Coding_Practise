class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        indp1 = []
        indp2 = []
        cocat = []
        iter = min(len(nums1), len(nums2))

        for i in range (0, len(nums1)):
            score = 0
            currentlyconsidered1 = nums1[i]
            if currentlyconsidered1 in nums2:
                
                score = score + 1
            
            if score == 0:
                
                indp1.append(nums1[i])
        
        for j in range (0, len(nums2)):
            score = 0
            currentlyconsidered2 = nums2[j]
            if currentlyconsidered2 in nums1:
                
                score = score + 1
            
            if score == 0:
                indp2.append(nums2[j])
        indp1 = list(dict.fromkeys(indp1))
        indp2 = list(dict.fromkeys(indp2))
        cocat = [indp1, indp2]
        return cocat



        