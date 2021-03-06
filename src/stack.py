class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

#LIFO - Last In First Out
class Stack:
	def __init__(self):
	#ref to the head node of our linked list
		self.head = None

	def push(self, val):
		#adds the val as the new head of linked list
		new_node = Node(val)
		#connect the new node to the current head
		new_node.next = self.head
		#set the head reference to refer to the new node
		self.head = new_node
		
	def pop(self):
		#check if the stack is empty
		if not self.head:
			#this is an empty stack
			return None
		#take another reference to the current head
		old_head = self.head
		#returns the value stored at the head
		self.head = self.head.next
		#and moves the head reference to the next linked list node
		return old_head.val

stack = Stack()

stack.push(11)
stack.push(14)
stack.push(15)

print(stack.pop())
print(stack.pop())
print(stack.pop())

def swap(nums):
  test = list(str(nums))

  for i in range(0, len(test) - 1, 2):
    test[i], test[i + 1] = test[i + 1], test[i]
  return int(''.join(test))

print(swap(12345))