
class Solution():

    def sellBuy(self,prices):
        if not prices:
            return 0
        max_profit = 0
        buy_price = prices[0]

        for p in prices:
            buy_price = min(buy_price,p)
            max_profit = max(max_profit, p - buy_price)
        return max_profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    sol = Solution()
    print(sol.sellBuy(prices))
