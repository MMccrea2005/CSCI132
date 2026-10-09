# This is the starter file for the Unordered List Assignment


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

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            else:
                current = current.next
        return False

    def remove(self, item):
        current = self.head
        previous = None
        
        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next
            
        if current is None: 
            raise ValueError(f'{item} is not on the list')
        
        #case: first item remove
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count


    def append(self, item):
        current = self.head
        previous = None
        while current is not None:
            previous = current
            current = current.next
        if current is None:
            previous.next = item

    def insert(self, pos, item):
        pass

    def index(self, item):
        current = self.head
        count = 0
        while current is not None:
            if item == current:
                break
        else:
            count = count + 1
            current = current.next
        
        print(count)
        return count
            
        
                
                

    def pop(self):
        current = self.head
        previous = None
        while current.next is not None:
            previous = current
            current = current.next

        if current.next == None:
            previous.next = None
                
        return current


# helper for printing/development
def printUnord(theList):
    current = theList.head
    while current is not None:
        print(f"{str(current.data)} ", end="")
        current = current.next
    print()


def main():

    myList = UnorderedList()
    
    myList.add(31)
    myList.add(77)
    myList.add(17)
    myList.add(93)
    myList.add(26)
    myList.add(54)
    
    printUnord(myList)

    # add test cases for each method here
    # myList.remove(54)
    # myList.remove(31)
    # myList.remove(93)
    
    # myList.pop()
    # myList.append(55)
    myList.index(93)
    printUnord(myList)


main()
