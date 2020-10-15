class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.res = []
        self.make('', characters, combinationLength)
    def make(self, char, characters, combinationLength):
        if not combinationLength:
            self.res.append(char)
            return
        for index,each in enumerate(characters):
            self.make(char+each, characters[index+1:], combinationLength-1)
    def next(self) -> str:
        return self.res.pop(0)
    def hasNext(self) -> bool:
        try:
            if self.res[0]:
                return True 
        except IndexError:
            return False
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()