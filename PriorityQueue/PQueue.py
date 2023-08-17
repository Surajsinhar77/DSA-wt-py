
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