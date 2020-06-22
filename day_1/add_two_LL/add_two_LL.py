# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
create an list to store the summed digits
    - add the head of l1/l2 together, push the value into the digits list
    - continue to traverse l1/l2 summing the values and pushing to the digits list
    - after the traversal is complete, check to see if any values are >= 10 (which is 2 digits)
        - If the value is >= 10, subtract 10 from that value and add 1 to the value of the next index
        - If there is not a value at the next index, push 1 to the digits array
    - Iterate over the digits list again, turning it into a Linked List
    - Return the new Linked List
'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Create a list to hold the summed digits of l1/l2
        summed_digits = list()
        
        curr1 = l1
        curr2 = l2
        
        # Traverse the linked lists, pushing the sum of their values to the summed_digits list
        while curr1 is not None and curr2 is not None:
            summed = curr1.val + curr2.val
            summed_digits.append(summed)
            
            curr1 = curr1.next
            curr2 = curr2.next
            
        # Iterate over the summed_digits list
        for i in range(len(summed_digits)):
            value = summed_digits[i]
            
            # Check if the value is a 2 digit number 
            if value >= 10:
                
                # Subtract 10 from the value
                value -= 10
                summed_digits[i] = value
                
                # Check if there is a next index in the array
                if i + 1 >= len(summed_digits):
                    
                    # If there is not, appened the digit 1
                    summed_digits.append(1)
                    
                else:
                    # If there is, add one to the value of the next index
                    summed_digits[i + 1] += 1
                    
        ll = ListNode(summed_digits[0])
        prev_node = ll
        
        # Iterate over the summed_digits list again to turn it into a Linked List
        for i in range(1, len(summed_digits)):
            node = ListNode(summed_digits[i])
            
            prev_node.next = node
            prev_node = node
            
        # Return the Linked List
        return ll
            
            