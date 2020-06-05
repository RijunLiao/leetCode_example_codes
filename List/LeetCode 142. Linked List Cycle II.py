# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        #s={}
        slow=head
        fast=head
        if not head or not head.next: return None
        if fast.next==fast: return head
        while fast:
            if not fast.next: return None
            #slow_index=slow.next
            slow=slow.next
            fast=fast.next.next
            if fast==slow: 
                slow=head
                while slow!=fast:                    
                    slow=slow.next
                    fast=fast.next
                return slow
        return None    
        
'''
        if not head or not head.next:
            return None
        if head.next==head:
            return head
        
        slow=head
        fast=head.next
        
        while fast and fast.next:
            if slow==fast:
                # if cycle is found return the slow pointer to head of list and move slow and fast pointer at same rate
                slow=head
                while slow!=fast.next:                    
                    slow=slow.next
                    fast=fast.next
                return slow
                
            else:
                #fast pointer moves at double the speed of slow pointer
                slow=slow.next
                fast=fast.next.next
        return None
'''
