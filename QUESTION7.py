def coin_change(coins, target_sum):
    num_coins = len(coins)
    dp = [[0 for _ in range(target_sum + 1)] for _ in range(num_coins + 1)]
    for i in range(num_coins + 1):
        dp[i][0] = 1
    for i in range(1, num_coins + 1):
        for j in range(1, target_sum + 1):
            if coins[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
    return dp[num_coins][target_sum]

# Test case
coins = [1, 2, 5]
target_sum = 5
ways = coin_change(coins, target_sum)
print("Number of ways to make the target sum:", ways)
