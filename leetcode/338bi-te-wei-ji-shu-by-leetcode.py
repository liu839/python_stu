class Solution:
    def countBits(self, num):
        res = [0]
        dict_visited ={0:0}
        flag = 0
        for i in range(1,num+1):
            temp =  dict_visited.get(i-flag,1)
            if not (i&i-1):
                flag = i
                res.append(1)
                dict_visited[i] = 1
            else:
                res.append(1+temp)
                dict_visited[i] = 1+temp
        return res
print(Solution().countBits(8))