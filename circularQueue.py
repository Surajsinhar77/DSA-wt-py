
class CQueue:
    def __init__(self, size):
        self.queue = [None]*size
        self.front = 0
        self.rear = 0
        self.size = 0
        self.cap = size

    def Enque(self, data):
        if(self.size < self.cap):
            self.queue[self.rear] = data
            self.size+=1
            self.rear = (self.rear+1)%self.cap # 1%1
            return
        print("size is Full")

    
    def Deque(self):
        if(self.size <= 0):
            print("Empty Queue")
            return
        data = self.queue[self.front]
        self.queue[self.front] = None
        self.front+=1
        self.size-=1
        return data

    def Dispay(self):
        if(self.size !=0 ):
            print(self.queue)


ob  = CQueue(5)
ob.Enque(5)
ob.Enque(6)
ob.Enque(7)
ob.Enque(9)
ob.Enque(11)

ob.Deque()
ob.Deque()
ob.Deque()
ob.Deque()
ob.Enque(1)
ob.Dispay()


