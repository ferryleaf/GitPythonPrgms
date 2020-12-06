#342 + 465 = 807
class ListNode(object):
    def __init__(self,object):
        self.val=object
        self.next=None

class Solution():
    def add_linked_list(l1,l2):
        l1_lst=l2_lst=''
        sum=0
        for ele in l1:
            l1_lst = str(ele) + l1_lst
        for ele in l2:
            l2_lst = str(ele) + l2_lst
        sum=str(int(l1)+int(l2)).reverse()
        for ele in str(sum):
            print(ele)

if __name__=='__main__':
    sol = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    sol.add_linked_list(l1,l2)
