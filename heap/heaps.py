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
    def initList(self, _array):
        if (not self.array) :
            self.array.append("#")
        self.array.extend(_array)
        self.__buildHeap(self.array)
    #private methods
    def __swap(self, _list, index1, index2):
        temp = _list[index1]
        _list[index1] = _list[index2]
        _list[index2] = temp
    def __climb(self, indexElem):
        pai = indexElem//2
        if pai >= 1 :
            if self.array[indexElem] > self.array[pai]:
                self.__swap(self.array,indexElem,pai)
                self.__climb(pai)

    def __descend(self, indexElem):
        j = indexElem*2
        if (j < len(self.array)-1) :
            if self.array[j+1] > self.array[j] :
                j += 1
        if (j <= len(self.array) -1) and (self.array[j] > self.array[indexElem]) :
            self.__swap(self.array,indexElem,j)
            self.__descend(j)


    #O(n)
    def __buildHeap(self, array):
        # for (int i = n/2; i > 0; i--)
        for i in range((len(self.array)-1)//2, 0, -1):
            self.__descend(i)
    #O(n/2)
    def __buildHeap2(self, array):        
        for i in range(2,len(array)-1):
            self.__climb(i)

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

    def heapSort(_list):
        if (len(self.array) > 1) :
            self.__swap(self.array[1], self.array[len(self.array)-1])
            _list.append(self.array.pop())
            self.__descend(1)
            heapSort()

    def delete(self):
        self.array.clear()

def display(_list):
    print("[", end="")
    for i in _list:
        print(i, end=",")
    print("]")