class Empty(Exception):
    pass


class Stack:
    def __init__(self):
        self.mylist = []

    def lengths(self):
        return len(self.mylist)

    def is_empty(self):
        if self.lengths() == 0:
            return True
        else:
            return False

    def push(self, ele):
        self.mylist.append(ele)

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is Empty")
        else:
            return self.mylist.pop()

    def top(self):
        return self.mylist[-1]

    def display(self):
        if(self.lengths() == 0):
            print("Stack is Empty")
        else:
            return self.mylist


if __name__ == '__main__':
    ss = Stack()
    print("display", ss.display())
    ss.push(5)
    ss.push(6)
    ss.push(7)
    print("display", ss.display())
    print("is_empty", ss.is_empty())
    print("display", ss.display())
    print("top", ss.top())
    print("pop", ss.pop())
    print("top", ss.top())
    print("display", ss.display())
