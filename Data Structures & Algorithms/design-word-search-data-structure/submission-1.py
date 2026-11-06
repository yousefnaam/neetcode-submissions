class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEOW = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEOW = True
        

    def search(self, word: str) -> bool:
        cur = self.root

        return self.dfs(0,word,cur)
    
    def dfs(self,i,word,cur):

        if i == len(word):
            return cur.isEOW

        char = word[i]
        if char == ".":
            for child in cur.children.values():
                if self.dfs(i + 1, word, child):
                    return True
            return False
        if char not in cur.children:
            return False
        return self.dfs(i + 1, word, cur.children[char])


        
        



        
