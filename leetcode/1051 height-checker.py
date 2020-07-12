 def heightChecker(heights: List[int]) -> int:
     res=sorted(heights)
     sum_=0
     for i in range(len(heights)):
         if heights[i] != res[i]:
             sum_+=1
    return sum_/2
