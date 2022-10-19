# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_node(prev_node):
    prev_node.next = prev_node.next.next
    
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        left = head
        right = head
        
        while right.next:
            right = right.next
            if right.val != left.val:
                left.next = right
                left = right
            else:
                delete_node(left)
             
        return head
        
        
        
