class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.stacka = []
        self.stackb = []

    """
    @param: element: An integer
    @return: nothing
    """

    def push(self, element):
        # write your code here
        self.stacka.append(element)

    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        if self.stackb == []:
            while self.stacka:
                self.stackb.append(self.stacka.pop())
            return self.stackb.pop()
        else:
            return self.stackb.pop()

    """
    @return: An integer
    """

    def top(self):
        # write your code here
        if self.stackb:
            top = self.stackb.pop()
            self.stackb.append(top)
            return top
        else:
            return self.stacka[0]