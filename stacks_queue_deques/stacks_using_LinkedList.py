'''
Implement Stack using LinkedList
'''

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Stack(Node):
    def __init__(self,val=0):
        super().__init__(val)

    def display(self):
        print(self.val)



'''
    def push(self,val):
        self.val=val

    def pop(self):

    def top(self):

    def is_empty(self):
'''

if __name__=='__main__':
    stk=Stack()
    stk=Stack(3)
    #stk.push(3)
    stk.display()
