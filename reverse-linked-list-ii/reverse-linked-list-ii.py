# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse_ll(head: Optional[ListNode], max_switches: int) -> Optional[ListNode]:
    """
    Reverse a simply linked list.
    """
    curr = head
    prev = None

    idx = 0
    while curr and idx <= max_switches:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        idx += 1
        
    return prev, next_node


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        1. Find the ``before`` node if it exists
        
        2. Reverse the list from ``left`` to ``right``
        
        3. Link ``before`` ``next_node`` of list reversal
        """
        # change to 0 index
        left -= 1
        right -= 1
        # if left == 0, then there is no prior beginning and the new list starts at left
        # then before == left?
        ptr = head
        before = None
        
        index_list = 0
        while ptr:
            if index_list == (left-1):
                before = ptr
                
            # reverse between left and right
            if index_list >= left and index_list < right:
                num_elem = right - left
                initial = ptr # first element of the reversed sequence, which is going to be last
                reversed_list, next_node = reverse_ll(ptr, num_elem)

                
                index_list = right

                if before:
                    before.next.next = next_node
                    before.next = reversed_list
                else:
                    initial.next = next_node
                    head = reversed_list
                break # we are done
            
            ptr = ptr.next
            index_list += 1
            
            
        return head