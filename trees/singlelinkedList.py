class Node:
    def __init__(self):
        self.data = None
        self.next = None
    #setting data field for the node
    def setData(self,data):
        self.data=data
    #getting data filed
    def getData(self):
        return self.data

    #method to setting next field of the node
    def setNext(self,next):
        self.next=next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next!=None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node
    def __str__(self):
        s = ""
        p = self.head
        if p != None:
            while p.next != None:
                s += p.data
                p = p.next
            s += p.data
        return s

    def search(self, k):
        p = self.head
        if p != None:
            while p.next != None:
                if (p.data == k):
                    return p
                p = p.next
            if (p.data == k):
                return p
        return None

    def remove(self, p):
        tmp = p.prev
        p.prev.next = p.next
        p.prev = tmp


    def listLength(self):
        current=self.head
        count=0
        while current!=None:
            count=count+1
            current=current.getNext()
        return count

    #At Begiining
    def insertAtBeginning(self,data):
        newNode=Node()
        newNode.setData(data)
        if self.listLength()==0:
            self.head=newNode
        else:
            newNode.setNext(self.head)
            self.head=newNode
    #At End
    def insertAtEnd(self,data):
        newnode=Node()
        newnode.setData(data)
        current=self.head
        if self.listLength()==0:
            self.head=newnode
        else:
            while current.getNext()!=None:
                current=current.getNext()
            current.setNext(newnode)

    def insertAtAnyPosition(self, data,pos):
        if pos >self.listLength() or pos < 0:
            return None
        else:
            if pos==0:
                self.insertAtBeginning(data)
            else:
                if pos==self.listLength():
                    self.insertAtEnd(data)
                else:
                    newnode = Node()
                    newnode.setData(data)
                    count=0
                    current = self.head
                    while count<pos-1:
                        count=count+1
                        current=current.getNext()
                    newnode.setNext(current.getNext())
                    current.setNext(newnode)
    #delete 1st Node:
    def deleteAtFirst(self):
        if self.listLength()==0:
            None
        else:
            self.head=self.head.getNext()
    def deleteAtEnd(self):
        if self.listLength()==0:
            return "list is empty"
        else:
            current = self.head
            previous=self.head
            while current.getNext()!=None:
                previous=current
                current=current.getNext()
            previous.setNext(None)
    def deleteAtAnyPosition(self,pos):
        if self.listLength()==0:
            return "list is empty"
        elif pos >self.listLength() or pos < 0:
            return None
        else:
            current = self.head
            previous=self.head
            count=0
            while count <pos-1:
                previous=current
                current=current.getNext()
            previous.setNext(None)
    def traverse(self):
        current=self.head
        while current!=None:
            print current.getData()
            current=current.getNext()



    # example code
l = LinkedList()

#l.add('a')
#l.add('b')
#l.add('c')

print l.listLength()
l.insertAtBeginning('1')
l.insertAtBeginning('2')
l.insertAtBeginning('3')
l.insertAtBeginning('4')
print l.listLength()
l.insertAtEnd('5')
print l.listLength()
l.insertAtAnyPosition('6',1)
print l.listLength()
print "traverse"
print l.traverse()
print "traverse"
l.deleteAtFirst()
print l.traverse()
print "traverse"
l.deleteAtEnd()
print l.traverse()