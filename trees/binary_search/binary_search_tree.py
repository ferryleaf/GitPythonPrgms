# https://www.educative.io/edpresso/binary-trees-in-python
# Deletion : https://www.javatpoint.com/deletion-in-binary-search-tree
# Insertion/Deletion/Search time complexity is O(h) : h = height of the tree
# Search : log n : n = number of nodes
class Node:
    def __init__(self, ele):
        self.ele = ele
        self.left = None
        self.right = None

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

    # Find the left most node to the node(to be deleted)
    def delete(self, ele):
        node = self.search(ele)
        if node:
            subs_node = node.find_left_most_node()
            temp = node
            node.left = subs_node.left
            node.right = subs_node.right
            subs_node.left = temp.left
            subs_node.right = temp.right
        else:
            return "Unable to find the number"

    def find_left_most_node(self):
        if self.left is None:
            return self
        else:
            self.left.find_left_most_node()

    # Binary Search Tree
    def search(self, ele):
        if self.ele == ele:
            print("Yes")
            ptr = self
            return id(ptr)
        else:
            if ele < self.ele:
                if self.left is not None:
                    self.left.search(ele)
                else:
                    print("No")
                    return None
            else:
                if self.right is not None:
                    self.right.search(ele)
                else:
                    print("No")
                    return None

    # Print all Nodes in Tree (Infix Traversal)
    def PrintNode(self):
            if self.left:
                self.left.PrintNode()
            print(self.ele, end=" ")
            if self.right:
                self.right.PrintNode()


# 12 6 14 3
# 1 2 3 4 5 6
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

    root.PrintNode()
    print()
    root.search(6)

    # Use the insert method to add nodes
    print()
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(31)
    root.insert(10)
    root.insert(19)

    root.PrintNode()
    print()
    pp = root.search(14)
    print(root.search(14))
    # print(pp.ele, pp.left.ele, pp.right.ele)
