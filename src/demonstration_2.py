"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.

As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.

The Stack class that you will use has been provided to you.
"""
class Stack:
    def __init__(self):
        self.data = []

    #method to get the length of the stack
    def __len__(self):
      return len(self.data)
        
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"

class QueueTwoStacks:
  def __init__(self):
    #holds the elements in the in_stack in the reversed order
    #when we call the dequeue method we'll pop from this atack
    self.out_stack = Stack()
    #holds the incoming enqueues elements
    self.in_stack = Stack()
  
  def enqueue(self, item):
    self.in_stack.push(item)

  def dequeue(self):
    #we need to check if the oustack is empty
    #otherwise, just pop from the top of the `out_stack`
    #if it is, we'll empty the `in_stack` into the `out_stack` in reverse order
    if len(self.out_stack) == 0:
      #empty the contents of the `in_stack` into the `out_stack`
      while len(self.in_stack) != 0:
        popped = self.in_stack.pop()
        self.out_stack.push(popped)
    
    return self.out_stack.pop()
        
q = QueueTwoStacks()
print(q.dequeue())
q.enqueue(3)
q.enqueue(6)
print(q.dequeue())
q.enqueue(7)
q.enqueue(8)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

# from collections import deque

# class QueueTwoStacks:
#     def __init__(self):
#       self.data = deque()
        
#     def enqueue(self, item):
#       self.data.append(item)

#     def dequeue(self):
#       if len(self.data) > 0:
#         return self.data.pop()
#       return 'The stack is empty'
