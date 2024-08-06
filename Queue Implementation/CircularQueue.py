class Queue:
    def __init__(self, limit, fp=0, rp=-1, size=0):
        self.items = ["" for _ in range(limit)]
        self.limit = limit
        self.size = size
        self.fp = fp
        self.rp = rp

    def setfp(self, fp):
        self.fp = fp
    
    def getfp(self):
        return self.fp
    
    def setrp(self, rp):
        self.rp = rp
    
    def getrp(self):
        return self.rp
    
    def setsize(self, size):
        self.size = size

    def getsize(self):
        return self.size

    def IsEmpty(self):
        return self.size ==  0
    
    def IsFull(self):
        return self.size == self.limit
    
    def Enqueue(self, item):
        if self.IsFull() == True:
            return "Queue Overflow"
        else:
            if self.rp == self.limit:
                self.rp = 1
            else:
                self.rp += 1
            self.items[self.rp] = item
            self.size += 1
            return str(self.items) + "   front ptr-> " + str(self.fp) + "   rear ptr->" + str(self.rp) + "  Limit->" + str(self.limit) + "  Size->" + str(self.size)

    def Dequeue(self):
        if self.IsEmpty() == True:
            return "Empty queue. Nun to dequeue"
        else:
            deleted_item = self.items[self.fp]
            self.items[self.fp] = "DELETED"
            self.size -= 1
            if self.fp == self.limit:
                self.fp = 1
            else:
                self.fp += 1
            return str(self.items) + "  front ptr->" + str(self.fp) + "  rear ptr->" + str(self.rp) + "  DELETED ITEM:" + str(deleted_item) + "  Limit->" + str(self.limit) + "  Size->" + str(self.size)
        
    
queue = Queue(5)
print(queue.Enqueue(1))
print(queue.Enqueue(2))
print(queue.Enqueue(3))
print(queue.Enqueue(4))
print(queue.Enqueue(5))
print(queue.Enqueue(6))
print(queue.Dequeue())