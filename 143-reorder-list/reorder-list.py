# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        current=slow.next
        slow.next=None
        prev=None
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        first=head
        second=prev
        while second:
            first_next=first.next
            second_next=second.next
            first.next=second
            second.next=first_next
            first=first_next
            second=second_next




        