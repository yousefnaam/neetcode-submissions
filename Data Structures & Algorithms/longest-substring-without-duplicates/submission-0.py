class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #iterate through our string and verify if it exists in a set
        #if it doesnt, we add to set and update max length of set
        #zxyxyz

        myset = set()
        longest = 0;
        ptr1 = 0
        ptr2 = 0

        while ptr2 < len(s):
            if s[ptr2] not in myset:
                myset.add(s[ptr2])
                longest = max(longest, len(myset))
                ptr2+=1
            else:
                myset.remove(s[ptr1])
                ptr1 += 1
        return longest






        