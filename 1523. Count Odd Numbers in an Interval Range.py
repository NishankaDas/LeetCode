class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        if high == low and high%2 == 0:
            return 0
        elif high == low and high %2 == 1:
            return 1
        k = high - low + 1
        
        if k == 1:
            return 1
        k = k/2
        if low%2 == 1 and high%2 == 1:
            return k+1
        else:
            return k
