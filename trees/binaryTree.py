class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

left = Tree(2)
right = Tree(3)
tree = Tree(1, left, right)
print tree.cargo,tree.left,tree.right

#Preorder
def print_tree(tree):
    if tree == None: return
    print tree.cargo,
    print_tree(tree.left)
    print_tree(tree.right)

tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))
#print print_tree(tree)

#Postorder
def print_tree_Post(tree):
    if tree == None: return
    print_tree(tree.left),
    print_tree(tree.right)
    print tree.cargo

tree1 = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))
#print print_tree_Post(tree1)



#Inorder
def print_tree_inorder(tree):
    if tree == None: return
    print_tree_inorder(tree.left)
    print tree.cargo,
    print_tree_inorder(tree.right)
tree2= Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))
#print print_tree_inorder(tree2)

def print_tree_indented(tree, level=0):
    if tree == None: return
    print_tree_indented(tree.right, level+1)
    print '  ' * level + str(tree.cargo)
    print_tree_indented(tree.left, level+1)

tree3= Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))
#print print_tree_indented(tree3)