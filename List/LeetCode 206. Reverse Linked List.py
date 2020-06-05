# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        # method 1: stack
        s=[]
        dummy=tail=ListNode(0)
        while head:
            s.append(head.val)
            head=head.next
        while s:
            tail.next=ListNode(s.pop())
            tail=tail.next
            
        return dummy.next
        '''
        # method 2
        prev, curr, nxt = None, head, None
        '''
        nxt=curr.next
        curr.next=prev
        
        prev=curr
        curr=nxt
        
        nxt=curr.next
        curr.next=prev

        prev=curr
        curr=nxt
        '''
        while curr:
            nxt=curr.next
            curr.next=prev

            prev=curr
            curr=nxt            
        
        return prev
'''
Time complexity: O(n)

Space complexity: O(1)        
'''