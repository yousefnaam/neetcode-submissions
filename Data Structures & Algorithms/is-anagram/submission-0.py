class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = [0] * 26

        for char in s:
            scount[ord(char) - ord('a')] +=1
        
        for char in t:
            if scount[ord(char) - ord('a')] == 0:
                return False
            scount[ord(char) - ord('a')] -=1
        
        for i in range(26):
            if scount[i] != 0:
                return False
        return True
        


        