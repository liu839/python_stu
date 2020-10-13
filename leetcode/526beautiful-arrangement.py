class Solution:
    def make(self, list_num, lens):
        if not list_num:
            self.num+=1
        for index,each in enumerate(list_num):
            if (not each % (lens+1)) or (not (lens+1) % each):
                list_temp = list_num[:]
                del list_temp[index]
                self.make(list_temp, lens+1)

    def countArrangement(self, N: int) -> int:
        self.num = 0
        self.make([each for each in range(1,N+1)],0)
        return self.num