class node:
    def __init__(self):
        self.data=None
        self.next=None
    def getData(self):
        return self.data
    def setData(self,data):
        self.data=data

    def setNext(self,next):
        self.next=next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next!=None

class LinkedList:
    def __init__(self):
        self.head=None
    def listLength(self):
        current=self.head
        count=0
        while current!=None:
            current=current.getNext()
            count+=1
        return count
    def addAtBegining(self,data):
        newnode=node()
        newnode.setData(data)
        if self.listLength()==0:
            self.head=newnode
        else:
            newnode.setNext(self.head)
            self.head=newnode
    def traversal(self):
        if self.listLength()==0:
            return None
        else:
            current=self.head
            while current!=None:
                print current.getData()
                current=current.getNext()
    def deleteNthPosition(self,pos):
        if self.listLength()==0:
            return
        else:
            count=0
            previous=self.head
            current=previous.getNext()
            while count!=pos-1:
                previous=current
                current=current.getNext()
                count+=1
            temp=current.getNext()
            previous.setNext(temp)
            current=temp
    def deleteNthValue(self,value):
        if self.listLength()==0:
            return
        else:
            previous=self.head
            current=previous.getNext()
            while (current.getData()!=value):
                previous=current
                current=current.getNext()
            temp=current.getNext()
            previous.setNext(temp)
            current=temp
mylist=LinkedList()
mylist.addAtBegining('5')
mylist.addAtBegining('3')
mylist.addAtBegining('8')
mylist.addAtBegining('18')
mylist.addAtBegining('1')
mylist.addAtBegining('16')
mylist.addAtBegining('8')
mylist.addAtBegining('3')
print "######Length#########"
print mylist.listLength()
print "######Traversal#########"
print mylist.traversal()
print "######Remove nth position#########"
mylist.deleteNthPosition(4)
print mylist.traversal()
print "######Remove nth value#########"
mylist.deleteNthValue('18')
print mylist.traversal()
