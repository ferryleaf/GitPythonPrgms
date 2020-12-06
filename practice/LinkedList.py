class Empty(Exception):
    pass


class LinkedList:
    class Node:
        def __init__(self, ele):
            self.ele = ele
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.lengths() == 0

    def lengths(self):
        return self.count

    def add(self, ele):
        self.count += 1
        if self.head is None:
            self.head = self.Node(ele)
            self.tail = self.head
        else:
            self.tail.next = self.Node(ele)
            self.tail = self.tail.next

    def remove(self):
        if (self.is_empty()):
            raise Empty("LinkedList is Empty")
        else:
            val = self.head.ele
            self.head = self.head.next
            self.count -= 1
        return val

    def display(self):
        print("Length:", self.count)
        if(not self.is_empty()):
            temp = self.head
            while(temp):
                print("temp:", temp.ele)
                temp = temp.next
        else:
            return (": LinkedList is Empty")


if __name__ == '__main__':
    ll = LinkedList()
    print("display", ll.display())
    ll.add(5)
    ll.add(6)
    ll.add(7)
    ll.add(8)
    ll.display()
    print("remove", ll.remove())
    ll.display()
    ll.add(9)
    print("remove", ll.remove())
    print("remove", ll.remove())
    ll.display()
    print("remove", ll.remove())
    print("remove", ll.remove())
    ll.display()
