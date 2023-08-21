class trieNode:

    def __init__(self, data):
        self.data = data
        self.child = [None]*26
        self.finish = False

class trie:
    # root = None
    def __init__(self):
        self.root = trieNode('\0')
    
    def __insert(self, root ,word):
        if word == '':
            root.finish = True
            return
        
        index = ord(word[0])-ord('a')
        if(root.child[index] == None):
            trieNewNode = trieNode(word[0])
            root.child[index] = trieNewNode
        self.__insert(root.child[index], word[1:])

    def insertWord(self,word):
        self.__insert(self.root, word)

ob = trie()
ob.insertWord("ant")
print("Done ")
