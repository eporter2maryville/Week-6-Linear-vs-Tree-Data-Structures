# Name: Brent Porter
# GitHub ID: eporter2maryville
# Assignment: 6.2 Build Heap Method

from random import *

#place holder for the list of random numbers
randomNumberList=[]

#creates a list of random integers between 1 and 100. If a dulicate is created it is not added to the list
#The result is a list of 10 or less unique random numbers
def createList(listOfNumbers):
    workingList=listOfNumbers
    for index in range(10):
        random = randrange(1,101)
        if random not in workingList:
            workingList.append(random)
        print(workingList)
    return workingList

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval


    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1


def main():
    #random list of numbers created and printed before the heap tree is created
    createList(randomNumberList)
    BrentHeap=BinHeap()
    
    BrentHeap.buildHeap(randomNumberList)
    
    for index in range(len(randomNumberList)):
        print(BrentHeap.delMin())
    
main()