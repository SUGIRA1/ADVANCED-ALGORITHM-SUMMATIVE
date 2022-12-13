def countcoinswithsamesum(coins, n, sum):

	if (sum == 0):
		return 1
	if (sum < 0):
		return 0
	if (n <= 0):
		return 0
	return countcoinswithsamesum(coins, n - 1, sum) + countcoinswithsamesum(coins, n, sum-coins[n-1])
# Driver program to test above function
coins = [2, 5, 3, 6]
n = len(coins)
print(countcoinswithsamesum(coins, n, 10))
