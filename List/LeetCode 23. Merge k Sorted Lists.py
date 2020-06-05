# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        curr = head = ListNode(0)
        queue = []
        count = 0
        for l in lists:
            if l is not None:
                count += 1
                heapq.heappush(queue, (l.val, count, l))
        while len(queue) > 0:
            _, _, curr.next = heapq.heappop(queue)
            curr = curr.next
            if curr.next is not None:
                count += 1
                heapq.heappush(queue, (curr.next.val, count, curr.next))
        return head.next   
'''
Time complexity: O(nklogk), sort => O(logk)
Space complexity: O(k) + O(nk)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        priority_queue=[]
        count=0
        dummy=tail=ListNode(0)
        for i in range(len(lists)):
            if lists[i]:    # to make sure lists[i] is not None
                heapq.heappush(priority_queue,(lists[i].val,count,lists[i]))
                count=count+1
        while priority_queue:
            _,_,tail.next=heapq.heappop(priority_queue)
            tail=tail.next
            if tail.next:
                heapq.heappush(priority_queue,(tail.next.val,count,tail.next))
                count=count+1                
        return dummy.next


#==========method 2============
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq
def mergeTwoLists(l1,l2):
    dummy=tail=ListNode(0)
    while l1 and l2:
        if l1.val<l2.val:
            tail.next=l1
            l1=l1.next
        else:
            tail.next=l2
            l2=l2.next
        tail=tail.next
    if l1: 
        tail.next=l1 
    elif l2: 
        tail.next=l2
    return dummy.next

#def divide_conquer(lists): # not int start and int end
def divide_conquer(lists, start, end):
    if start>end: return None
    if start==end: return lists[start]
    if start+1==end: return mergeTwoLists(lists[start],lists[end])
    #m=start+(end-start)//2
    m=int(start+(end-start)/2)
    l1=divide_conquer(lists,start,m)
    l2=divide_conquer(lists,m+1,end)
    return mergeTwoLists(l1,l2)
    
    
class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l=divide_conquer(lists,0,len(lists)-1)
        
        return l
'''
Time complexity: O(nklogk)
Space complexity: O(logk)
'''