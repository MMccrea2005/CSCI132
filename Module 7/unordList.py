class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, node_data):
        """Set node data"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, node_next):
        """Set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        """String"""
    
class UnorderedList:

    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def add(self,item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        # print('at end of add')
        
    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            else:
                current = current.next
        return False
    
    def remove(self):
        pass
    
    def size(self):
        pass
    
    def append(self, item):
        pass
    
    #insert, index, pop

# helper for printing/development
def printUnord(theList):   
    
    current = theList.head
    
    while current is not None:
        print(f'{str(current.data)} ',end='')
        current = current.next
    print()
    
def main():
    
    myList = UnorderedList()
    
    myList.add(31)
    myList.add(77)
    printUnord(myList)
    print(myList.search(42))
    
main()
    