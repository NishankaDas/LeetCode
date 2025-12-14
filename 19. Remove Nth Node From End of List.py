class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Step 1: compute length
        ct = 0
        k = head
        while k:
            ct += 1
            k = k.next
        
        # If removing first node
        if n == ct:
            return head.next
        
        # Step 2: move to node BEFORE the one to delete
        k = head
        for _ in range(ct - n - 1):
            k = k.next
        
        # Delete
        k.next = k.next.next
        return head
