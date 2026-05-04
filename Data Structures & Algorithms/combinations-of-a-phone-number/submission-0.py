class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        letter = {
             "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtrack(start,string):
            if len(string) == len(digits):
                res.append(string)
                return
            for c in letter[digits[start]]:
                backtrack(start+1, string + c)
        if digits:
            backtrack(0,"")
        return res

        