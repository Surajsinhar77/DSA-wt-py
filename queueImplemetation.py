# class Queue:
#     def __init__(self):
#         self.queue = []
#         self.front = -1
#         self.rear = -1

#     def enqueue(self, data):
#         self.queue.append(data)
#         self.rear += 1
#         if(len(self.queue) > 1):
#             self.front = 0
#         print(len(self.queue))

#     def dequeue(self):
#         if len(self.queue) == 0 :
#             print("Queue is empty")
#             return -1
#         if(len(self.queue) > 1):
#             item = self.queue[self.front]
#         else:
#             item = self.queue[self.front+1]
#         self.queue.pop(0)
#         print("Deleted item:", item)
#         if(len(self.queue) == 0):
#             self.rear = -1
#             self.front = -1
#         else:
#             self.rear-=1


#     def get_rear(self):
#         if self.rear == -1:
#             return -1
#         return self.queue[self.rear]

#     def isEmpty(self):
#         if(self.rear == self.front):
#             return False
#         else:
#             return True
        
#     def get_front(self):
#         if(self.isEmpty()):
#             if(len(self.queue) > 1):
#                 return self.queue[self.front]
#             else:
#                 return self.queue[0] 
#         else:
#             print("Queue is empty")
#             return -1 

#     def display(self):
#         if len(self.queue) == 0:
#             print("Queue is empty")
#         else:
#             print("Front data:", self.get_front())
#             print("Rear data:", self.get_rear())
#             print("Elements ",self.queue)


# ob = Queue()
# ob.enqueue(2)
# ob.dequeue()
# ob.enqueue(4)
# ob.dequeue()
# ob.enqueue(7)
# ob.enqueue(8)
# ob.enqueue(9)
# ob.enqueue(11)
# ob.enqueue(3)
# ob.dequeue()
# print("front of queue : ", ob.get_front())

# ob.display()


h = [0]*7

import array as ary


g = ary.array('i', [0]*8)



print(g)

# print(len(h))
# print(h)
# h[len(h)-1] = 8


# print(h)