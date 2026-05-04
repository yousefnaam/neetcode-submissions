class Solution:
    def isPalindrome(self, s: str) -> bool:

        r = len(s) - 1
        l = 0
        slow = s.lower()

        while(l < r):
            while not slow[l].isalnum() and l < r:
                l+= 1
            while not slow[r].isalnum() and l < r:
                r-= 1
            if slow[l] != slow[r]:
                return False
            else:
                l+=1
                r-= 1
        return True

            



        