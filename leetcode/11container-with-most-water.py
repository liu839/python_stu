class Solution:
    def maxArea(self, height: List[int]) -> int:
        lens = len(height)
        i, j = 0, lens-1
        res = min(height[i],height[j])*(j-i)
        while j > i:
            if height[i]>=height[j]:
                j -= 1
            else:
                i += 1
            res=max(min(height[i],height[j])*(j-i), res)
        return res
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         area=0
#         high=len(height)-1
#         low=0
#         max_number=(low,high)
#         max_area=0
#         while True:
#             if low>=high:
#                 break
#             area=min(height[low],height[high])*(high-low)
#             if area>max_area:
#                 max_number=(low,high)
#                 max_area=area
#             if height[low]<height[high]:
#                 low+=1
#             else:
#                 high-=1
#         return max_area
        