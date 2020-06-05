# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''
        slow=ListNode(0)
        slow.next=head
        fast=ListNode(0)
        fast.next=head
        while slow:
            slow=slow.next
            fast=fast.next.next
            if slow==fast: return 0
        return -1
        '''
        slow=fast=head

        while fast:
            if not fast.next: return False
            slow=slow.next
            fast=fast.next.next
            if slow==fast: return True
        return False        
#Fast + Slow pointers
'''
Time complexity: O(n)

Space complexity: O(1)
'''