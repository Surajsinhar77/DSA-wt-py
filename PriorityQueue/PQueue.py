
class PriorityQueue:
    pq = []

    def __init__(self):
        self.pq =[]

    def isEmpty(self):
        return self.pq
    
    def PqSize(self):
        return len(self.pq)
    
    def getMin(self):
        if(self.isEmpty()):
            return 0
        return self.pq[0]
    
    def insert(self , element ):
        self.pq.append(element)

        childInd = len(self.pq)-1

        while(childInd > 0):
            parentIndex = childInd-1//2
            if(self.pq[childInd] < self.pq[parentIndex]):
                temp = self.pq[childInd]
                self.pq[childInd] = self.pq[parentIndex]
                self.pq[parentIndex] = temp
            else:
                break
            childInd = parentIndex

    def removeMin(self):
        if(len(self.pq) < 1):
            return 0
        
        minValue = self.pq[0]
        self.pq[0] = self.pq[len(self.pq)-1]
        self.pq.pop()

        currentIndex = 0
        left = (currentIndex*2)+1 
        right = (currentIndex*2)+2

        while(currentIndex < left):
            if(self.pq[left] < self.pq[right]):
                if(self.pq[left] < self.pq[currentIndex]):
                    temp = self.pq[left]
                    self.pq[left] = self.pq[currentIndex]
                    self.pq[currentIndex] = temp
                    currentIndex = left
                else:
                    break
            else:
                if(self.pq[right] < self.pq[currentIndex]):
                    temp = self.pq[right]
                    self.pq[right] = self.pq[currentIndex]
                    self.pq[currentIndex] = temp
                    currentIndex = right
                else:
                    break
            left = (currentIndex*2)+1
            right = (currentIndex*2)+2