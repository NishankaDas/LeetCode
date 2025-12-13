import math
class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        ct = 0
        for i in range(1,n+1):
            for j in range(1,n+1):
                k = i**2 + j**2
                l = int(k**0.5)
                if l<= n and l*l == k:
                    ct += 1
        return ct

