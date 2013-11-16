import solution

def printbst(node, depth=0):
    print "%s Depth: %s, Value: %s" % ("  " * depth, depth, node.val)
    if node.left:
        printbst(node.left, depth+1)
    if node.right:
        printbst(node.right, depth+1)

bst = solution.BST()
bst.insert(5)
bst.insert(7)
bst.insert(1)
bst.insert(3)
bst.insert(2)
bst.insert(6)
bst.insert(20)
bst.insert(25)
print "Broken tree"
printbst(bst.root)


bst = solution.BST2()
bst.insert(5)
bst.insert(7)
bst.insert(1)
bst.insert(3)
bst.insert(2)
bst.insert(6)
bst.insert(20)
bst.insert(25)
print "Recursion"
printbst(bst.root)


bst = solution.BST3()
bst.insert(5)
bst.insert(7)
bst.insert(1)
bst.insert(3)
bst.insert(2)
bst.insert(6)
bst.insert(20)
bst.insert(25)
print "while loop"
printbst(bst.root)

bst = solution.BSTSum()
bst.insert(5)
bst.insert(7)
bst.insert(1)
bst.insert(3)
bst.insert(2)
bst.insert(6)
bst.insert(20)
bst.insert(25)
print "sumAtDepth"
print "3", bst.sumAtDepth(3)
print "2", bst.sumAtDepth(2)
print "1", bst.sumAtDepth(1)
print "5", bst.sumAtDepth(5)
