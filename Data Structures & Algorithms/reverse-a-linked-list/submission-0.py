# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head)
        if not head:
            return None
        # newNode=head
        # if head.next:
        #     newNode=self.reverseList(head.next)
        #     head.next.next=head
        # head.next=None
        # return newNode
        curr=head
        prev=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev