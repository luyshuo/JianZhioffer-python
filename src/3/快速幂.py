class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
        elif n == 1:
            return a % b
        else:
            remainder = self.fastPower(a, b, n // 2)
            remainder = remainder * remainder % b
            if n % 2 == 1:
                remainder = remainder * (a % b) % b
            return remainder
