import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        biggest_pile = max(piles)

        L, H = 1, biggest_pile

        res=H
        while L<=H:
            k = (L+H)//2

            hours_to_eat = 0
            for pile in piles:
                hours_to_eat += math.ceil(float(pile) / float(k))
            
            if hours_to_eat <= h:
                res = min(res,k)
                H=k-1   
            elif hours_to_eat>h:
                L=k+1

        return res
