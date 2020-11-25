class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, pos= 0, 0
        gas_ = gas[pos]
        lens = len(gas)
        des = (pos+1)%lens
        if sum(gas) < sum(cost):
            return -1
        while True:
            if gas_ >= cost[pos]:
                gas_ = gas_ - cost[pos] + gas[des]
                pos = des
                des = (pos+1)%lens
                if pos == start or des ==0:
                    return start
            else:
                start ,pos = des, des 
                des = (pos+1)%lens
                gas_ = gas[pos]