#########
# Stack #
#########

class Stack:
	def isEmpty(stack):
		return stack == []

	def push(stack, elmt):
		stack.append(elmt)

	def pop(stack):
		stack.pop()

	def top(stack):
		return stack[len(stack)-1]