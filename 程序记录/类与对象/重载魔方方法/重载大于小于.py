class Word(str):
    def __init__(self,string):
        if ' ' in string :
            string=string[:string.index(' ')]
        self.length=len(string)

    def __lt__(self,other):
        if self.length<other.length:
            return True
        return False

    def __gt__(self,other):
        if self.length>other.length:
            return True
        return False

    def __le__(self,other):
        if self.length<=other.length:
            return True
        return False

    def __ge__(self,other):
        if self.length>=other.length:
            return True
        return False

a=Word('fishc')
b=Word('i love fishc')

if a>b:
    print("a>b")
else:
    print("a<b")