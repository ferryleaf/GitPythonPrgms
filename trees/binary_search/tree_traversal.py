# Infix
# Prefix
# Postfix
class Node:
    def __init__(self,ele):
        self.ele = ele
        self.left = self.right = None

    def insert(self,ele):
        if self.ele is None:
            self.ele = Node(ele)
        else:
            if ele < self.ele:
                if self.left is None:
                    self.left = Node(ele)
                else:
                    self.left.insert(ele)
            else:
                if self.right is None:
                    self.right = Node(ele)
                else:
                    self.right.insert(ele)

    # Already Infix Traversal
    def PrintNode(self):
        if self.left:
            self.left.PrintNode()
        print(self.ele, end=" ")
        if self.right:
            self.right.PrintNode()

    # Prefix Traversal
    def prefix_traversal(self):
        print(self.ele, end=" ")
        if self.left:
            self.left.prefix_traversal()
        if self.right:
            self.right.prefix_traversal()

    # Postfix Traversal
    def postfix_traversal(self):
        if self.left:
            self.left.postfix_traversal()
        if self.right:
            self.right.postfix_traversal()
        print(self.ele, end=" ")


# 12 6 14 3
# 1 2 3 4 5 6
# 27 14 35 31 10 19
if __name__ == '__main__':
    # T = int(input("Enter number of runs:"))
    # for i in range(T):
    #     arr = list(map(int, input("Enter list of elements: ").strip().split()))
    #     for count,ele in enumerate(arr):
    #         if count == 0:
    #             root = Node(ele)
    #         else:
    #             root.insert(ele)
    #     root.PrintNode()

    # Use the insert method to add nodes
    root = Node(1)
    root.insert(2)
    root.insert(3)
    root.insert(4)
    root.insert(5)
    root.insert(6)

    print("\nInfix:")
    root.PrintNode()
    print("\nPrefix:")
    root.prefix_traversal()
    print("\nPostfix:")
    root.postfix_traversal()

    # Use the insert method to add nodes
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(31)
    root.insert(10)
    root.insert(19)

    print("\nInfix:")
    root.PrintNode()
    print("\nPrefix:")
    root.prefix_traversal()
    print("\nPostfix:")
    root.postfix_traversal()
