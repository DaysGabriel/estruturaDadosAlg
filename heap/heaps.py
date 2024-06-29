"""
1. __init__
2. __swap
3. __climb
4. __descend
5. __buildHeap
6. __buildHeap2
7. insert
8. delete b
9. update
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
    #public methods
    def insert(self, elem) :
        self.array.append(elem)
        self.__climb(len(self.array))
    
    def delete(self) :
        self.__swap(self.array, 1, len(self.array))
        self.array.pop()
        self.__descend(1)

    def update(self, i, newValue):
        if (newValue > self.array[i]):
            self.array[i] = newValue
            self.__climb(self,i)
        elif (newValue < self.array[i]):
            self.array[i] = newValue
            self.__descend(self,i)

    def heapSort(self,_list):
        if (len(self.array) > 1) :
            self.__swap(self.array, 1, len(self.array))
            _list.append(self.array.pop())
            self.__descend(1)
            self.heapSort(_list)

    def delete(self):
        self.array.clear()

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
        if (j < len(self.array)) :
            if self.array[j+1] > self.array[j] :
                j += 1
        if (j <= len(self.array)) and (self.array[j] > self.array[indexElem]) :
            self.__swap(self.array,indexElem,j)
            self.__descend(j)
    #O(n)
    def __buildHeap(self, array):
        # for (int i = n/2; i > 0; i--)
        for i in range(len(self.array)//2, 0, -1):
            self.__descend(i)
    #O(nlog_{n})
    def __buildHeap2(self, array):        
        for i in range(2,len(array)):
            self.__climb(i)

def display(_list):
    print("[", end="")
    for i in _list:
        print(i, end=",")
    print("]")
