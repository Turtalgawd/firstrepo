class Queue:
    def __init__(self, max_size, fp=0, rp=-1):
        self.items = ["" for _ in range(max_size)]
        self.max_size = max_size
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


    def IsEmpty(self):
        return self.rp ==  -1
    
    def IsFull(self):
        return self.rp == self.max_size -1
    
    def Enqueue(self, item):
        if self.IsFull() == True:
            return "Queue Overflow"
        else:
            self.rp += 1
            self.items[self.rp] = item
            return str(self.items) + "   front ptr-> " + str(self.fp) + "   rear ptr->" + str(self.rp)

    def Dequeue(self):
        if self.IsEmpty() == True:
            return "Empty queue. Nun to dequeue"
        else:
            deleted_item = self.items[self.fp]
            self.items[self.fp] = "DELETED"
            self.fp += 1
            self.max_size -= 1
            return str(self.items) + "  front ptr->" + str(self.fp) + "  rear ptr->" + str(self.rp) + "  DELETED ITEM:" + str(deleted_item)
        
    
queue = Queue(5)
print(queue.Enqueue(1))
print(queue.Enqueue(2))
print(queue.Enqueue(3))
print(queue.Enqueue(4))
print(queue.Enqueue(5))
print(queue.Enqueue(6))
print(queue.Dequeue())

