# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        plus = 0

    # Initialize curr with head of Linked List
        curr = head

    # Traverse till we reach None
        while curr is not None:
        # Increment count by 1
            plus += 1

        # Move pointer to next node
            curr = curr.next
        index = plus / 2
        
        index = floor(index)
        if plus == 1:
            return None
        

        removal = head
        previous = None
        
        tracker = 0

        while removal is not None:
            if tracker == index:
                break
            previous = removal
            removal = removal.next
            tracker = tracker + 1
        previous.next = removal.next
        return head

        

        
        