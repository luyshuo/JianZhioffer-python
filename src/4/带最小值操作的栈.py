class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.stackmin = []

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        # write your code here
        self.stack.append(number)
        if self.stackmin == []:
            self.stackmin.append(number)

        else:
            min = self.stackmin[-1]
            if number < min:
                min = number
            self.stackmin.append(min)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        if self.stack != []:
            m = self.stack.pop()
            self.stackmin.pop()
            return m

    """
    @return: An integer
    """

    def min(self):
        # write your code here
        return self.stackmin[-1]
