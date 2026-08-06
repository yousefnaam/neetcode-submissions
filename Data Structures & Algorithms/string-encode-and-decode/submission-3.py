class Solution:

    """ 
    input list of strings, need to turn into a single string,
    encode:
    turn list of strings into a single string
    string has a length
    could potentially use length as a way to decode,

    strs = ["#Hello","World"]
    5#Hello5World
    




    """

    def encode(self, strs: List[str]) -> str:

        newstring = ""

        for s in strs:
            newstring+= str(len(s)) + "#" + s
        return newstring

    def decode(self, s: str) -> List[str]:

        ptr = 0
        ans = []

        while ptr < len(s):
            num = ""
            while s[ptr] != "#":
                num+= s[ptr]
                ptr+=1
            num = int(num)
            ans.append(s[ptr+1:ptr+num+1])
            ptr+=num+1
        return ans

"""
strs = ["Hello","World"]
newstring= 5#Hello5#World

ptr=0
num=5


"""
