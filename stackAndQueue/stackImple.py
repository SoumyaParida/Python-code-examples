class stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    def insert(self,data):
        self.items.append(data)
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def show(self):
        return self.items

s=stack()
print s.isEmpty()
s.insert('8')
s.insert('2')
s.insert('5')
s.insert('1')
s.insert('18')
print s.size()
print s.show()
s.pop()
print s.show()
print s.peek()
print s.show()



