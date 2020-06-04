# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry_bit=0
        dummy_head=tail=ListNode(0)
        while l1 or l2 or carry_bit==1: # while l1 or l2 or carry_bit: is also correct
            '''
            if l1==None: 
                l1_val=0 
            else: 
                l1_val=l1.val
            if l2==None: 
                l2_val=0 
            else: 
                l2_val=l2.val
            sum_=l1_val+l2_val+carry_bit
            '''
            sum_=(l1.val if l1 else 0)+(l2.val if l2 else 0)+carry_bit # simple, s+=s+l1.val
            tail.next=ListNode(sum_%10)
            tail=tail.next
            carry_bit=sum_//10
            #if l1.next!=None: l1=l1.next # error
            #if l2.next!=None:  l2=l2.next # error
            if l1!=None: l1=l1.next # right
            if l2!=None:  l2=l2.next # right            
            
        return dummy_head.next

'''
Time Complexity: O(max(n,m))
Space Complexity: O(max(n,m))

'''

'''
Runtime: 72 ms, faster than 70.51% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.9 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.
'''