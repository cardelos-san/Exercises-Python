
#Given an array of stock prices, find the most profit you can make with a single transaction
#Each index represents a different day for that stock price
#A transaction consists of purchasing a stock and selling it a different day
#Time complexity: O(n^2)
#Space complexity: O(n)

priceList = [5, 11, 3, 50, 60, 90]

def maxProfit(prices):
    max_profit = 0
    current_profit = 0
    length = len(prices)
    
    for i in range(length):
        j = i + 1
        while(j < length): 
            current_profit = abs(prices[i] - prices[j])
            if current_profit > max_profit:
                max_profit = current_profit
                optimal_buy = prices[i]
                optimal_sell = prices[j] 
            j = j + 1
    print(prices)
    print("The max profit you can make is", max_profit, "if you buy at", optimal_buy,
     "and sell at", optimal_sell)
     
if __name__ == "__main__":
    maxProfit(priceList)