# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None: return head # if not head or not head.next: return head
        dummy=ListNode(0)
        dummy.next=head
        head=dummy
        while head.next and head.next.next:
            n1,n2=head.next,head.next.next
            n1.next=n2.next
            n2.next=n1
            head.next=n2
            head=head.next.next # or head=n1
            
            '''# wrong order, should use revise order to switch
            head.next=n2
            n2.next=n1
            n1.next=head.next.next.next
            head==head.next.next
            '''
        return dummy.next
'''
Time Complexity: O(n)
Space Complexity: O(1)

'''            