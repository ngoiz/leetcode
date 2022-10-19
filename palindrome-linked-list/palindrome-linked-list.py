# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Three-step approach:
        1. Find the middle of the linked list with slow and fast pointers
        2. Reverse the second half of the list
        3. Iterate through second half comparing to original head. If discrepancy, no palindrome
        """
        
        # find second half
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second_half = slow
        # print('Second half', second_half)
        
        # reverse second half
        curr = second_half
        prev = None  # this is the reversed second half
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # print('Reversed second half', prev)
            
        # iterate through reversed second half
        while prev:
            # print('Checking...')
            # print(prev.val, head.val)
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
            
        return True
        