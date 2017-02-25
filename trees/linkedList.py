class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

def print_list(node):
    while node:
        print node,
        node = node.next
    print


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next=node3

print_list(node1)

def print_backward(list) :
    if list == None : return
    print_backward(list.next)
    print list,

print_backward(node1)