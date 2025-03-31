class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1 = headA
        curr2 = headB
        
        has_set = set()
        
        while curr1:
            has_set.add(curr1)
            curr1 = curr1.next
            
        while curr2:
            if curr2 in has_set:
                return curr2
            curr2 = curr2.next
        
        return None
        
        
