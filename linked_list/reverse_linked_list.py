'''
Reverse a Linked List
Google:

Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?

Example:
Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL

class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

  # Function to print the list
  def printList(self):
    node = self
    output = ''
    while node != None:
      output += str(node.val)
      output += " "
      node = node.next
    print(output)

  # Iterative Solution
  def reverseIteratively(self, head):<
 /span>
    # Implement this.

  # Recursive Solution
  def reverseRecursively(self, head):
    # Implement this.

# Test Program
# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseIteratively(testHead)
#testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    # Iterative Solution : 4 3 2 1 0 :: 0 1 2 3 4
    def reverseIteratively(self, head):
        node = head
        temp1 = ''
        temp2 = ''
        while(node!=None):
            if (node == head):
                temp1 = node.next
                head.next = None

            if (temp1.next!=None):
                temp2 = temp1.next
                temp1.next = node
                node = temp1
                temp1 = temp2
            else:
                temp1.next = node
                node = None


    # Recursive Solution : 4 3 2 1 0 :: 0 1 2 3 4
    def reverseRecursively(self, head):
        node = head
        if (node.next == None):
            return node

        temp = node.reverseRecursively(node.next)
        temp.next = node
        if (node == self):
            node.next = None
        return node



# Test Program
# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0

testHead.reverseIteratively(testHead)
testHead.reverseRecursively(testHead)

print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4
