class Solution(object):
    def numTrees(self, n):
        import math 
        numer = math.factorial(2*n)
        denom = math.factorial(n+1)*math.factorial(n)

        return (int(numer/denom))
