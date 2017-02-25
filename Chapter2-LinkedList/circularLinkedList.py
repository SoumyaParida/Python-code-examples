class Node:
    def __init__(self):
        self.data=None
        self.next=None
    def getData(self):
        return self.data
    def setData(self,data):
        self.data=data

    def getNext(self):
        return self.next
    def setNext(self,next):
        self.next=next

class CircularLinkedList:
    def __init__(self):
        self.head=None
    def addElement(self,data):
        ptr1 = Node()
        ptr1.setData(data)
        temp = self.head
        ptr1.next = self.head
        # If linked list is not None then set the next of
        # last node
        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = ptr1
        else:
            ptr1.next = ptr1  # For the first node
        self.head = ptr1
    def traversal(self):
        temp = self.head
        if self.head is not None:
            while (True):
                print temp.data
                temp = temp.next
                if (temp == self.head):
                    break


mylist=CircularLinkedList()
mylist.addElement('4')
print mylist.traversal()
mylist.addElement('14')
print mylist.traversal()
mylist.addElement('2')
print mylist.traversal()

