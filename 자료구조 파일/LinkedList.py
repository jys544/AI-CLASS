# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 13:26:51 2023

@author: user
"""

class ListNode: 
    
   def __init__(self, newItem, nextNode):
       self.item = newItem
       self.next = nextNode


class LinkedListBasic:
    
    def __init__(self):
        #__head = 첫 번째 노드에 대한 래퍼런스
        self.__head = ListNode('dummy', None)
        #__numItems = 연결 리스트에 들어 있는 원소의 총 수
        self.__numItems = 0
#insert(i,x)=x를 리스트의 i번 원소로 삽입
    def insert(self, i:int, newItem):
        if i >= 0 and i <= self.__numItems:
            prev =self.__getNode(i-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1
        else:
          print("index",i , ": out of bound in insert()") #    
#맨끝추가
    def append(self, newItem):
            prev = self.__getNode(self.__numItems - 1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1
#삭제
    def pop(self, i:int):
        if(i >= 0 and i <= self.__numItems - 1):
            prev = self.__getNode(i - 1)
            curr = prev.next
            prev.next = curr.next
            retItem = curr.item
            self.__numItems -= 1
            return retItem
        else: 
            return None
    def remove(self, x):
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next
            self.__numItems -= 1
            return x
        else:
            return None
# get(i)=i번 원소를 알려준다
    def get(self, i:int):
        if self.isEmpty():
            return None
        if(i >= 0 and i <= self.__numItems - 1):
            return self.__getNode(i).item
        else:
            return None
# index(X)=원소 x가 리스트의 몇번 원소인지 알려준다
    def index(self, x) -> int:
        curr = self.__head.next
        for index in range(self.__numItems):
            if curr.item == x:
                return index
            else:
                curr = curr.next
        return -12345
# 빈리스트인지 알려준다
    def isEmpty(self) -> bool:
      return self.__numItems == 0
# 총 원소 수를 알려준다
    def size(self) -> int:
      return self.__numItems
# 리스트를 청소한다
    def clear(self):
      self.__head = ListNode("dummy", None)
      self.__numItems = 0      
# 원소 x 가 몇 번 나타나는지 알려준다
    def count(self, x) -> int:
      cnt = 0
      curr = self.__head.next
      while curr != None:
            if curr.item == x:
                   cnt += 1
            curr = curr.next
      return cnt
#extend(a)=리스트에 나열할 수 있는 객체 a를 풀어서 추가한다
    def extend(self, a): #여기서 a는 self와 같은 타입의 리스트
          for index in range(a.size()):
                 self.append(a.get(index))
#리스트를 복사해서 새 연결 리스트르 리턴한다
    def copy(self):
      a = LinkedListBasic()
      for index in range(self.__numItems):
            a.append(self.get(index))
      return a
#순서를 역으로 뒤집는다
    def reverse(self):
      a = LinkedListBasic()
      for index in range(self.__numItems):
            a.insert(0, self.get(index))
      self.clear()
      for index in range(a.size()):
            self.append(a.get(index))
 #정렬
    def sort(self) -> None:
      a = []
      for index in range(self.__numItems):
            a.insert(0, self.get(index))
      a.sort()
      for index in range(len(a)):
            self.append(a[index])
        
    def __findNode(self, x) ->(ListNode, ListNode):
        prev = self.__head
        curr = prev.next
        while curr != None:
              if curr.item == x:
                      return(prev,curr)
              else:
                      prev = curr; curr = curr.next
        return(None,None)
    def __getNode(self, i:int) -> ListNode:
          curr = self.__head # dummy head, index: 1
          for index in range(i+1):
            curr = curr.next
          return curr
    def printList(self):
        curr = self.__head.next
        while curr != None:
            print(curr.item, end="")
            curr = curr.next
    print()
    
#LinkedList test

list = LinkedListBasic()
list.append(30)
list.insert(0, 20)
a = LinkedListBasic()
a.append(4)
a.append(3)
a.append(3)
a.append(2)
a.append(1)
list.extend(a)
list.reverse()
list.pop(0)
print("count(3):", list.count(3))
print("get(2):", list.get(2))
list.printList()