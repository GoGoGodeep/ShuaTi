class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        if not head:
            return

        curr = head
        pre = None

        while curr:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp
        
        return pre
