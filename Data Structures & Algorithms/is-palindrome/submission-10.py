class Solution:
    def isPalindrome(self, s: str) -> bool:

        """
        string reads forwards and backwards, input string is Case-Sesitive, Ignores all alpha numeric
        Two-Pointer -> 1 front, 1 back, while true converge, while its alphanum()
        while not alphanum,, move pointer up
        """

        r= len(s)-1
        l = 0

        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
        