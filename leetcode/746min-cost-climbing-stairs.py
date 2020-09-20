class Solution:
    def minCostClimbingStairs(self, cost):
        lens = len(cost)
        if lens == 1:
            return 0
        cost_ = [0 for _ in range(lens+1)]
        cost_[0], cost_[1] = cost[0], cost[1]
        cost.append(0)
        point = 2
        while point <= lens:
                cost_[point] = min(cost_[point-1], cost_[point-2]) + cost[point]
                point+=1
        return cost_[-1]