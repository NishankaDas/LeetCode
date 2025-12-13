class Solution(object):
    def sortList(self, head):
        if not head:
            return head

        # Extract values
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        # Sort values
        arr.sort()

        # Write back
        curr = head
        for v in arr:
            curr.val = v
            curr = curr.next

        return head
