class Myrev:
    def __init__(self,string):
        self.string=list(string)
    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.string.pop()
        except IndexError:
            raise StopIteration

myrev=Myrev('Fishc')
for i in myrev:
    print(i,end='')