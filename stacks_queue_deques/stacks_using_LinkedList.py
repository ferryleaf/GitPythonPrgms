'''
Implement Stack using LinkedList

push(), pop(), isEmpty() and peek() all take O(1) time. We do not run any loop in any of these operations.

Create Basic Stack & it's functionalities

STACK: LIFO[LAST-IN-FAST-OUT]
FUNCTIONALITY:
    1.  PUSH
    2.  POP
    3.  IS_EMPTY
    4.  LENGTH
    5.  TOP
    
'''

class Node:
    def __init__(self, ele):
        self.ele = ele
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0

    def size(self):
        return self.length

    def push(self, ele):
        self.length += 1
        if self.head is None:
            self.head = Node(ele)
        else:
            node = Node(ele)
            node.next = self.head
            self.head = node
        return ("Pushed",  ele)

    def pop(self):
        if self.isEmpty():
            return "Empty"
        else:
            num = self.head.ele
            self.head = self.head.next
            self.length -= 1
            return ("Pop ", num)

    def isEmpty(self):
        return self.size() == 0

    def top(self):
        if not self.isEmpty():
            return self.head.ele

    def display(self):
        if not self.isEmpty():
            ptr = self.head
            for i in range(self.size()):
                print(ptr.ele, end=" ")
                ptr = ptr.next
        else:
            print("Empty")

if __name__ == '__main__':
    s = Stack()
    print("size", s.size())
    print("isEmpty", s.isEmpty())
    print("pop", s.pop())
    print("top", s.top())
    print("push", s.push(5))
    print("top", s.top())
    print("size", s.size())
    print("isEmpty", s.isEmpty())
    print("display", s.display())
    print("push", s.push(51))
    print("push", s.push(45))
    print("display", s.display())
    print("size", s.size())
    print("isEmpty", s.isEmpty())
    print("pop", s.pop())
    print("top", s.top())
    print("display", s.display())
