from queue_code import queue
import time
import threading

food_order_queue = queue()

def place_order(orders):
    for order in orders:
        print("Placing order for:",order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)


def serve_order():
    while True:
        if food_order_queue.size() == 0:
            break
        order = food_order_queue.dequeue()
        print("Now serving: ",order)
        time.sleep(2)

orders = ['pizza','samosa','pasta','biryani','burger']
t1 = threading.Thread(target=place_order, args=(orders,))
time.sleep(1)
t2 = threading.Thread(target=serve_order)

t1.start()
t2.start()