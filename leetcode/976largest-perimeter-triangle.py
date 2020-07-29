class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A)-2):
            if A[i+1]+A[i+2]>A[i]:
                return sum(A[i:i+3])
        return 0
            
            
            
            
            
            