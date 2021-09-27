class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        numer = math.factorial(2*n)
        denom = math.factorial(n+1)*math.factorial(n)

        return (int(numer/denom))
