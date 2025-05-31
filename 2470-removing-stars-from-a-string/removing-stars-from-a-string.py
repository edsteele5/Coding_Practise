class Solution:
    def removeStars(self, s: str) -> str:
        i = 0
        stars = s.count("*")
        while stars != 0:
            if s[i] == "*":
                
                s = s[:i] + s[i+1:]
                s = s[:i-1] + s[i:]
                stars = stars - 1
                i = i-2
            i = i+1
                
            
        return s
        