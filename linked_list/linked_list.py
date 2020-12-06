'''
How to create a linked list
Inserting Element at the head of Single LinkedList

'''


class Empty(Exception):
    pass


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val):
        self.head = Node(val, self.head)
        self.size += 1

    def pop(self):
        if (self.is_empty()):
            return Empty('Linked List is Empty')
        else:
            self.head = self.head.next
            self.size -= 1

    def insert_at_index(self, index, val):
        if (self.is_empty() and index > self.size):
            return Empty('Linked List is Empty, cannot insert at the index')
        elif ((self.is_empty()) or index == 0):
            self.push(val)
        elif (index <= self.size or (index == self.size + 1)):
            ptr = self.head
            for i in range(1, index):
                ptr = self.head.next
            temp = ptr.next
            ptr.next = Node(val, temp)
            self.size += 1
        else:
            return Empty('Index too Large')

    def is_empty(self):
        return self.size == 0

    def sizes(self):
        return self.size

    def display(self):
        print('*'*30)
        ptr = self.head
        while (ptr):
            print(ptr.val)
            ptr = ptr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.push(3)
    ll.push(4)
    ll.push(5)
    ll.push(6)
    ll.display()
    ll.pop()
    ll.display()
