'''
Double LinkedList


Operations: [Picked from https://www.javatpoint.com/doubly-linked-list]
a. Insert
    1. Insert at the begining
    2. Insert at the end
    3. Insert at the specified node
b. Delete
    1. Delete at the begining
    2. Delete at the end
    3. Delete at the specified node
c. Length
d. is_empty
e. traverse
f. display
'''


class Empty(Exception):
    pass


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.length() == 0

    def length(self):
        return self.size

    def extract_node_at_index(self, indx):
        if self.is_empty():
            return self.head
        else:
            cnt = 0
            temp = self.head
            while cnt < (indx-1):
                temp = temp.next
                cnt += 1
            return temp

    def insert(self, val, indx=None):
        print("Inserting value:", val, " at index:", indx)
        if self.is_empty():
            self.head = Node(val)
            self.head.prev = self.head
            self.size += 1
        else:
            if indx is None:
                indx = self.length()
            if ((self.length() < indx)):
                indx = self.length()

            if (indx == 0):
                temp1 =


            temp1 = self.extract_node_at_index(indx)
            temp2 = temp1.next
            temp1.next = Node(val)
            temp1.next.prev = temp1
            temp1.next.next = temp2
            self.size += 1

    def display(self):
        temp = self.head
        while(temp is not None):
            print(temp.val, end=',')
            temp = temp.next


if __name__ == '__main__':
    dll = DoubleLinkedList()
    print("is_empty", dll.is_empty())
    print("insert")
    dll.insert(5)
    dll.insert(6)
    print("length", dll.length())
    print("display")
    dll.display()
    print("is_empty", dll.is_empty())
    dll.insert(10, 2)
    print("display")
    dll.display()
    print("length", dll.length())
    dll.insert(3, 1)
    print("display")
    dll.display()
    print("length", dll.length())
    dll.insert(23, 0)
    print("display")
    dll.display()
    print("length", dll.length())
