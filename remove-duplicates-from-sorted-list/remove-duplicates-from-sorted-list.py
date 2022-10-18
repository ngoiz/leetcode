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
        ptr = head
        
        while ptr.next:
            if (ptr.next.val == ptr.val):
                delete_node(ptr)
            else:
                ptr = ptr.next

                
        return head
        
        
        
