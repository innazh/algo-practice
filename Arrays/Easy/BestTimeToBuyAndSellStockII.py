#first of all, THIS IS NOT "easy". LOL. 
#documenting some of my first attempts, solution might be simpler but I feel like the problem isn't phrased in the best way.
class Solution:
    def findSmallest(self, start, prices: List[int]):
        smoll = sys.maxsize
        idx = 0
        
        for i in range(start, len(prices)):
            if prices[i]<smoll:
                smoll = prices[i]
                idx = i
        return smoll, idx
    
    def maxProfit(self, prices: List[int]) -> int:
        day=0
        profit=0
        
        foundToSell=False
        while day<len(prices):
            #buy stock
            smallest = prices[day]
            boughtIdx = day
            #find when to sell
            print("h")
            while day<len(prices) and not foundToSell:
                if prices[day]>smallest:
                    print("Found when to sell stock I bought on day: " + str(boughtIdx))
                    print(", on price= " + str(smallest))
                    print("Selling at price: " + str(prices[day]) + ", of day " + str(day))
                    foundToSell=True
                    profit+=prices[day]-smallest
                else:
                    day+=1
            #if not found then buy stock the next day        
            if not foundToSell:
                print("Not found when to sell stock I bought on day: " + str(boughtIdx) + ", on price= " + str(smallest))
                day=boughtIdx+1
            else:
                foundToSell=False
                    
        return profit
            