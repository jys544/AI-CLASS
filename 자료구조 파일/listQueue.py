class ListQueue:
      def __init__(self):
            self.__queue = []
        
      def enqueue(self, x):
            self.__queue.append(x)
        
      def dequeue(self):
            return self.__queue.pop(0)
    
      def front(self):
            if self.isEmpty():
                   return None
            else:
                   return self.__queue[0]
    
      def isEmpty(self) -> bool:
            return (len(self.__queue) == 0)
    
      def dequeueAll(self):
            self.__queue.clear()
    
      def printQueue(self):
            print("queue from front:", end ='')
            for i in range(len(self.__queue)):
                  print()
        
q1 = ListQueue()
q1.enqueue("Mon")
q1.enqueue("Tue")
q1.enqueue(1234)
q1.enqueue("Wed")
q1.dequeue()
q1.enqueue('aaa')
q1.printQueue() 