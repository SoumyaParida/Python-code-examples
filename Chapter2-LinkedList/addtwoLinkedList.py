class node:
    def __init__(self,data=None,next=None):
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
                # Add contents of two linked lists and return the head

        # node of resultant list
    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0

        # While both list exists
        while (first is not None or second is not None):

            # Calculate the value of next digit in
            # resultant list
            # The next digit is sum of following things
            # (i) Carry
            # (ii) Next digit of first list (if ther is a
            # next digit)
            # (iii) Next digit of second list ( if there
            # is a next digit)
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            Sum = carry + fdata + sdata

            # update carry for next calculation
            carry = 1 if Sum >= 10 else 0

            # update sum if it is greater than 10
            Sum = Sum if Sum < 10 else Sum % 10

            # Create a new node with sum as data
            temp = node()
            temp.setData(Sum)

            # if this is the first node then set it as head
            # of resultant list
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

                # Set prev for next insertion
            prev = temp

            # Move first and second pointers to next nodes
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry > 0:
            temp.next = node(carry)

value=raw_input()
value1=value.split(' ')
print value1
newValue=0
count=0
mylist1= LinkedList()
value2=int(value1[0])
value3=int(value1[1])
while (value2):
    newValue=value2%10
    value2 = value2 / 10
    mylist1.addAtBegining(newValue)
print mylist1.traversal()

mylist2= LinkedList()
while (value3):
    newValue=value3%10
    value3 = value3 / 10
    mylist2.addAtBegining(newValue)
print mylist2.traversal()
# Add the two lists and see result
res = LinkedList()
res.addTwoLists(mylist1.head, mylist2.head)
print res.traversal()