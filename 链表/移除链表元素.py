class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def removeElements(self, head, val: int):
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy

    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next
