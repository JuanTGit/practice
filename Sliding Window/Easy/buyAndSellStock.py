# 121. Best Time to Buy and Sell Stock
# Easy

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Brute Force
def maxProfitBF(prices):
	res = 0

	for i in range(len(prices) - 1):
		for j in range(i+1, len(prices)):
			current = prices[j] - prices[i]
			res = max(res, current)
	return res

def maxProfit(prices):
    l, r = 0, 1
    max_profit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1
    return max_profit

print(maxProfit([7,1,5,3,6,4]))

def maxProfit2(prices):
    l = 0
    max_profit = 0
    for r in range(len(prices)):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
    return max_profit

print(maxProfit2([7,1,5,3,6,4,20,1,22]))

def maxProfit3(prices):
    max_profit = 0
    min_price = float('inf')
    for price in prices:
        min_price = min(price, min_price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit
        
maxProfit3([1 , 5, 7, -1, 2])