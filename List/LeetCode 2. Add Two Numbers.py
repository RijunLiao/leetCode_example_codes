# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry_bit=0
        dummy_head=tail=ListNode(0)
        while l1 or l2 or carry_bit==1:
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
            #if l1.next!=None: l1=l1.next # erro
            #if l2.next!=None:  l2=l2.next # erro
            if l1!=None: l1=l1.next # right
            if l2!=None:  l2=l2.next # right            
            
        return dummy_head.next
        