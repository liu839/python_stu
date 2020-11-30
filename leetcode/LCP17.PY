class Solution:
    def A(self):
        self.x = 2 * self.x + self.y
    def B(self):
        self.y = 2 * self.y + self.x
    def calculate(self, s: str) -> int:
        # self.x = 1
        # self.y = 0
        # s = list(s)
        # while s:
        #     temp = s.pop(0)
        #     if temp=="A":
        #         self.A()
        #     else:
        #         self.B()
        # return self.x+self.y
        return  2**len(s)