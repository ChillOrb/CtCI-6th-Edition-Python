import sys


class MultiStack:

    def __init__(self, stacksize):
        self.numstacks = 1
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize
        self.minvals = [sys.maxint] * (stacksize * self.numstacks)

    def Push(self, item, stacknum):
        if self.IsFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        if self.IsEmpty(stacknum):
            self.minvals[self.IndexOfTop(stacknum)] = item
        else:
            self.minvals[self.IndexOfTop(stacknum)] = min(
                item, self.minvals[self.IndexOfTop(stacknum) - 1])
        self.array[self.IndexOfTop(stacknum)] = item

    def Pop(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def Peek(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]

    def Min(self, stacknum):
        return self.minvals[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1


def StackMin():
    newstack = MultiStack(10)
    newstack.Push(5, 0)
    newstack.Push(6, 0)
    newstack.Push(2, 0)
    newstack.Push(7, 0)
    newstack.Push(14, 0)
    newstack.Push(3, 0)
    print newstack.Min(0)
    newstack.Push(1, 0)
    newstack.Push(4, 0)
    newstack.Push(44, 0)
    newstack.Push(2, 0)
    print newstack.Min(0)

StackMin()

''' Method 2: another stack to keep track of min element 



class StackWithMin:
    def __init__(self):

        self.mainStack = []

      
        self.trackStack = []

    def push(self, x):
        self.mainStack.append(x)
        if (len(self.mainStack) == 1):
            self.trackStack.append(x)
            return

       
        if (x < self.trackStack[-1]):
            self.trackStack.append(x)
        else:
            self.trackStack.append(self.trackStack[-1])

    def getMin(self):
        return self.trackStack[-1]

    def pop(self):
        self.mainStack.pop()
        self.trackStack.pop()


# Driver Code
if __name__ == '__main__':

    s = StackWithMax()
    s.push(20)
    s.push(23)
    s.push(60)
    s.push(700)
    print(s.getMin())

O(1) time
O(n) space
'''



