# Convert Tree into List/Queue
class Node:
    def __init__(self, ele):
        self.ele = ele
        self.left = None
        self.right = None

    # Inserting an Element into Tree in Binary Search Tree Style
    def insert(self, ele):
        if self.ele is None:
            self.ele = Node(ele)
        else:
            if ele < self.ele:
                if self.left:
                    self.left.insert(ele)
                else:
                    self.left = Node(ele)
            elif ele >= self.ele:
                if self.right:
                    self.right.insert(ele)
                else:
                    self.right = Node(ele)

    # Print all Nodes in Tree
    def PrintNode(self):
            if self.left:
                self.left.PrintNode()
            print(self.ele, end=" ")
            if self.right:
                self.right.PrintNode()

    # Level Order Traversal of Binary Tree/Binary Search Tree
    def level_order_traversal(self):
        lists = []
        if self.ele is None:
            return
        else:
            if len(lists) == 0:
                lists.append(self)
            node = self
            idx = 0

            while node is not None:
                if node.left is not None:
                    lists.append(node.left)
                if node.right is not None:
                    lists.append(node.right)
                idx += 1
                if idx != len(lists):
                    node = lists[idx]
                else:
                    break
            for node in lists:
                print(node.ele, end=" ")


if __name__ == '__main__':
    # Use the insert method to add nodes
    root = Node(1)
    root.insert(2)
    root.insert(3)
    root.insert(4)
    root.insert(5)
    root.insert(6)

    root.level_order_traversal()

    # Use the insert method to add nodes
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(31)
    root.insert(10)
    root.insert(19)
    # root.PrintNode()
    print()
    root.level_order_traversal()
