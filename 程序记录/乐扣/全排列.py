def solv(nums):
        if len(nums) == 0:
            return []
        used = [False for _ in range(len(nums))]
        res = []

        def dfs(nums, size, dep, path, used):
            #依次为总表,尺寸,递归深度,临时表,使用状态
            nonlocal res
            if dep == size:
                res.append(path[:])
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, dep + 1, path, used)

                    used[i] = False
                    path.pop()
        dfs(nums, len(nums), 0, [], used)

        return res
print(solv([1,2,3]))

"""
    def permute(self, nums: List[int]) -> List[List[int]]:
        def solv(temp, nums):
            if not nums:
                res.append(temp)
            else:
                for i, num in enumerate(nums):
                    solv(temp+[num], nums[:i]+nums[i+1:])
        
        res = []
        solv([], nums)
        return ans
"""
            
