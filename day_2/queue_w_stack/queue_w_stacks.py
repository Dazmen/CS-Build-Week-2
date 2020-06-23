from collections import deque

'''
    -Utilize two stacks
    - The first stack will end up being the "queue", the top will be the oldest item.
    - The second will be used for utility
    - when a new value is pushed to the que
        - pop all values in the first stack and add them to the second stack
        - then add the new value to the second stack 
        - pop all values off the second stack and add them back to the first stack
        - At this point the newest value will be at the bottom of the stack and the oldest at the top
    - peek & pop just need to look at the top of the first stack
'''

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Stack 1 will serve as the que, while stack 2 serves as the helper
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        
        # If Stack 1 is empty, just add the value to the "que" stack
        if len(self.stack1) == 0:
            self.stack1.append(x)
            
        else:
            
            # Otherwise, pop all the values from Stack1 and add them to stack2 (turning the stack upside-down)
            for _ in range(len(self.stack1)):
                num = self.stack1.pop()
                self.stack2.append(num)
                
            # Add the new value
            self.stack2.append(x)
            
            # Now pop all values from stack2 and add them to stack1 (turning the stack back to its original orientation)    
            for _ in range(len(self.stack2)):
                num = self.stack2.pop()
                self.stack1.append(num)
                
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        value = self.stack1.pop()
        return value

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack1) > 0:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()