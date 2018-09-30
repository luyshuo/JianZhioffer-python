class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """

    def fibonacci(self, n):
        # write your code here
        a = 0
        b = 1

        while n > 0:
            c = a
            a, b = b, a + b
            n = n - 1

        return c