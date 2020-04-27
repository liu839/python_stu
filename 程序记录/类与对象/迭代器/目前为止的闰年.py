class Leapyear:
    def __init__(self,year_stop=2020):
        self.year=0
        self.year_stop=year_stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.year==self.year_stop+1:
            raise StopIteration
        for _ in range(self.year,self.year_stop+1):
            self.year+=1
            if (self.year%4==0 and self.year%100!=0)or(self.year%400==0):
                return self.year
leap=Leapyear()
for each in leap:
    print(each)