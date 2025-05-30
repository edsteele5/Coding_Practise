class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currentalt = 0
        max_alt = currentalt
        for x in range (0, len(gain)):
            currentalt = currentalt + gain[x]


            if currentalt > max_alt:
                max_alt = currentalt
        
        return max_alt
        