class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        word3 = ""
        i = 0
        len1 = len(word1)
        len2 = len(word2)
        if len1 >= len2:
            lenA = len2
            wordloss = 1
        else:
            lenA = len1
            wordloss = 2
        
        word3 = word3 + word1[0]
        word3 = word3 + word2[0]
        
        for i in range(1, lenA):
            word3 = word3 + word1[i]
            word3 = word3 + word2[i]

            
        if wordloss == 1:
            for i in range(lenA, len(word1)):
                word3 = word3 + word1[i]
        elif wordloss == 2:
            for i in range(lenA, len(word2)):
                word3 = word3 + word2[i]
        return word3
