class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L=len(prices)
        if L<=1:
            return(0)
        else:
            max_first=[0]*L
            min_price=prices[0]
            max_profit_=0
            for i in range(1,L):
                profit_i=prices[i]-min_price
                if profit_i>=max_profit_:
                    max_first[i]=profit_i
                    max_profit_=profit_i
                else:
                    max_first[i]=max_profit_
                if prices[i]<min_price:
                    min_price=prices[i]
            min_second=[0]*L
            max_price=prices[L-1]
            min_profit_=float("inf")
            for i in range(L-2,1,-1):
                profit_i=prices[i]-max_price
                if profit_i<=min_profit_:
                    min_profit_=profit_i
                    min_second[i]=profit_i
                else:
                    min_second[i]=min_profit_
                if prices[i]>max_price:
                    max_price=prices[i]
            for i in range(1,L-1):
                two_=max_first[i]-min_second[i+1]
                if two_>max_profit_:
                    max_profit_=two_
            return(max_profit_)
