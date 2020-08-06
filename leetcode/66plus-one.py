class Solution:
    def plusOne(self, digits):
        i = -1
        digits[i] += 1
        while digits[i] == 10:
            digits[i] = 0
            i -= 1
            try:
                digits[i] += 1
            except IndexError:
                digits.insert(0,1)
                return digits
        return digits
                

print(Solution().plusOne([9]))