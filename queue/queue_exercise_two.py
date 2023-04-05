from queue_code import queue

q = queue()

# 1
# 
#
#

def print_binary_numbers(end):
    q = queue()
    q.enqueue("1")

    for _ in range(end):
        front = q.front()
        print(front)
        q.enqueue(front + "0")
        q.enqueue(front + "1")
        q.dequeue()

print_binary_numbers(50)