from collections import deque
def reverse(queue):
	Stack = []
	while (queue):
		Stack.append(queue[0])
		queue.popleft()

	while (len(Stack) != 0):
		queue.append(Stack[-1])
		Stack.pop()

queue=deque([10,20,30,40,50])
reverse(queue)
print()
print(queue)
print()