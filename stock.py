# Given a arry of integers, what is the largest possible positive difference between one of the integers and the integer before it? (By positive difference, I mean the second value is larger)
# The number could be anywhere between -500000 and 500000, and there could be any number of integers in the array.
# Example: [1 , 5, 7, -1, 2]
# Output: 6
# Explanation: While the smallest number is -1 and the largest is 7, -1 happens AFTER 7 and thus we don't consider this difference. The largest difference between an integer and an integer before it is between 7 and 1, thus 6.





def maxProfit(prices):
    max_profit = 0
    min_price = float('inf')
    for price in prices:
        min_price = min(price, min_price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit
        
maxProfit([1 , 5, 7, -1, 2])