# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # stack to save the value
        s1=[]
        s2=[]
        while l1:
            s1.append(l1.val)
            l1=l1.next
        while l2:
            s2.append(l2.val)
            l2=l2.next
            
        carry=0
        #dummy=ListNode(0) # can set dummy=None
        dummy=None
        while s1 or s2 or carry:
            s1_val=0
            s2_val=0
            if s1: s1_val=s1.pop()
            if s2: s2_val=s2.pop()
            carry+=s1_val+s2_val
            temp=ListNode(carry%10)
            temp.next=dummy
            dummy=temp
            carry=carry//10
        
        return dummy
'''
Time Complexity: O(l1+l2)
Space Complexity: O(max(l1,l2))

'''            