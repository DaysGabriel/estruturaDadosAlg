"""
usage: heap(MAXIMA), heap(MINIMA). A única diferença da máxima pra mínima é que uma compara
usando (>) e a outra usando (<) 
"""
"""
Methods I know are right:
1. __init__
2. insert
3. delete
4. update
5. __swap
6. __climb
"""

class MaxHeap:
    #constructor
    def __init__(self):
        self.array = ["#"]
    #private methods
    def __swap(self, _list, index1, index2):
        temp = _list[index1]
        _list[index1] = _list[index2]
        _list[index2] = temp
    def __climb(self, indexElem):
        if indexElem > 1 :
            if self.array[indexElem] > self.array[indexElem//2]:
                self.__swap(self.array,indexElem,indexElem//2)
                self.__climb(indexElem//2)

    def __descend(self, indexElem):
        j = indexElem*2
        if (j < len(self.array)+1) :
            if self.array[j+1] > self.array[j] :
                j += 1
            if (self.array[j] > self.array[indexElem]):
                self.__swap(self.array,indexElem,j)
                self.__descend(self, j)
    #public methods
    def insert(self, elem) :
        self.array.append(elem)
        self.__climb(len(self.array)-1)
    
    def delete(self) :
        self.__swap(self.array, 1, len(self.array)-1)
        self.array.pop()
        self.__descend(1)

    def update(self, i, newValue):
        if (newValue > self.array[i]):
            self.array[i] = newValue
            self.__climb(self,i)
        elif (newValue < self.array[i]):
            self.array[i] = newValue
            self.__descend(self,i)

myHeap = MaxHeap()

myHeap.insert(2)
myHeap.insert(3)
myHeap.insert(4)
myHeap.insert(5)
#myHeap.insert(0)
#myHeap.insert(1)

print(myHeap.array[0])
print(myHeap.array[1])
print(myHeap.array[2])
print(myHeap.array[3])