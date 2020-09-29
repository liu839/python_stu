def backpack(n, c, w, v):
    """
    n:有几个数据
    c:总容量
    w:物品占的容量
    v:物品的价值
    """
    dp = [[0 for _ in range(c+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, c+1):
            if j < w[i-1]:
                dp[i][j] = dp[i-1][j]
            if j >= w[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])
    return dp[-1][-1]
print(backpack(n = 5, c = 10, w = [2, 2, 6, 5, 4], v = [6, 3, 5, 4, 6]))