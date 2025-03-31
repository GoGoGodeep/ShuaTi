class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        list_len = 0
        temp = curr
        while temp:
            temp = temp.next
            list_len += 1
        
        for _ in range(list_len - n - 1):
            curr = curr.next
        
        curr.next = curr.next.next

        return dummy.next
