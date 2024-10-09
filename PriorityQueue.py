class PrioQ:
    '''Basic priority Queue Implementation'''
    def __init__(self):
        self.priorityQueue = {}
        self.minKey = 0
        self.maxKey = 10
        
    class PriorityQueueElement:
        def __init__(self,val,key):
            self.val = val
            self.key = key

    def Enqueue(self,val,key):
        Element = self.PriorityQueueElement(val,key)
        self.priorityQueue.setdefault(Element.key,[]).append(Element.val)
        self.priorityQueue.get(Element.key).sort()

    # def Dequeue(self):
    #     for i in range(self.minKey,self.maxKey+1):
    #         if i in self.priorityQueue:
    #             if len(self.priorityQueue[i]) >0:
    #                 val = self.priorityQueue[i][0]
    #                 del self.priorityQueue[i][0]
    #             return val
            
    def Dequeue(self):
        keys = self.priorityQueue.keys()
        #print(keys)
        keys = sorted(keys)
        for k in keys:
            if len(self.priorityQueue.get(k))==0:
                self.priorityQueue.pop(k)
            else:
                return self.priorityQueue.get(k).pop(0)
    

# pq = PrioQ()

# pq.Enqueue('Bob',1)
# pq.Enqueue('Jack',2)
# pq.Enqueue('Dylan',1)
# pq.Enqueue('Daniels',2)
# pq.Enqueue('Kevin',3)
# pq.Enqueue('Hart',3)

# print(pq.Dequeue())
# print(pq.Dequeue())
# pq.Enqueue('Ryan',1)
# print(pq.Dequeue())