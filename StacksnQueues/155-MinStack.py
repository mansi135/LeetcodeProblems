class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        if len(self.stack2) == 0 or self.stack2[-1] >= x:
            self.stack2.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack1) != 0:
            print(len(self.stack1), len(self.stack2))
            if self.stack1[-1] == self.stack2[-1]:
                self.stack2.pop()

            self.stack1.pop()

    def top(self):
        """
        :rtype: int
        """

        if len(self.stack1) == 0:
            return None

        return self.stack1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack2) == 0:
            return None

        return self.stack2[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()




# Alternate_solution without using extra stack
class MinStack_alternate(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

        if len(self.stack1) == 0:
            self.stack1.append((x, x))

        else:
            curr_min = self.stack1[-1][1]
            self.stack1.append((x, min(x, curr_min)))

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack1) != 0:
            self.stack1.pop()

    def top(self):
        """
        :rtype: int
        """

        return self.stack1[-1][0]

    def getMin(self):
        """
        :rtype: int
        """

        return self.stack1[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()