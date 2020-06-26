# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
    -Create two pointers to walk the lists
    - initialize an empty array
    - create a while loop (while pointer a or b is not null/none/false)
        - compare the value at the two pointers.
        - push the lesser value to the array.
        - increment the pointer
    - turn the array back into a LL
    
    2nd Pass
        - Same thing except cut out the array aspect
        - Create a variable that will hold the current 'tail' of the LL instead of an array
        - assign the lesser value being compared in the while loop to the next pointer of the current tail
        - then make that node itself the current tail
        - return that LL
    
'''

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # initializing head, curr_tail and pointer variables
        LL_head = None
        curr_tail = None
        
        # Check to ensure both lists have a value, if not return the other list
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
            
        
        pointer1 = l1
        pointer2 = l2
        
        
        # While both pointers are not none, start merging
        while pointer1 is not None and pointer2 is not None:
            
            # Initializing variables that represent the node values
            num1 = pointer1.val
            num2 = pointer2.val
            
            # Declaring a variable that will represent the lowest value node
            lowest = pointer1 if num1 <= num2 else pointer2
                
            # Check to ensure that LL_head and curr_tail have been initialized with a value
            if LL_head is not None:
                
                # set the next pointer of the current tail to the lowest value node, and then set that node to the curr_tail
                curr_tail.next = lowest
                curr_tail = lowest
                    
            # If the LL_head is not yet initialized (first pass), initialize the head/tail variables with the lowest value node
            else:
                LL_head = lowest
                curr_tail = lowest
                
            # Move set the pointer for the lowest value node to the next node it is connected to
            if lowest is pointer1:
                pointer1 = pointer1.next
            else:
                pointer2 = pointer2.next
        
        # Check to see which list has any remaining nodes to traverse
        remainder = pointer1 if pointer1 else pointer2
        
        # Add the remaining nodes to the end of the list
        while remainder is not None:
            curr_tail.next = remainder
            curr_tail = remainder
            remainder = remainder.next
            
        # Return the list
        return LL_head
        
