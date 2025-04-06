from collections import deque

class Node:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        dq = deque()
        dq.append(root)

        while dq:
            level = len(dq)
            prev = None

            for i in range(level):
                node = dq.popleft()

                if prev:
                    prev.next = node
                
                prev = node

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return root
