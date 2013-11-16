# First pass; completely failed with the 'tree' aspect, and wrote what I
# described as a binary search tuple.
class BST:
    root = None
    def insert(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
        else:
            if self.root.val < val:
                self.root.right = node
            else:
                self.root.left = node


class BST2:
    root = None
    def __init__(self):
        self.root = None
    def traverse(self, cur, val):
        if val < cur.val and cur.left:
            return self.traverse(cur.left, val)
        elif val < cur.val:
            return cur
        elif cur.right:
            return self.traverse(cur.right, val)
        else:
            return cur
    def insert(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
        else:
            leaf = self.traverse(self.root, val)
            if val < leaf.val:
                leaf.left = node
            else:
                leaf.right = node

# Asked to rewrite traverse() without recursion
class BST3:
    root = None
    def __init__(self):
        self.root = None
    def traverse(self, cur, val):
        while (cur.left and val < cur.val or cur.right and val >= cur.val):
            if val < cur.val:
                cur = cur.left
            if cur.right and val >= cur.val:
                cur = cur.right
        return cur        
    def insert(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
        else:
            leaf = self.traverse(self.root, val)
            if val < leaf.val:
                leaf.left = node
            else:
                leaf.right = node

# Create a sumAtDepth function
class BSTSum:
    root = None
    def __init__(self):
        self.root = None
    def traverse(self, cur, val):
        while (cur.left and val < cur.val or cur.right and val >= cur.val):
            if val < cur.val:
                cur = cur.left
            if cur.right and val >= cur.val:
                cur = cur.right
        return cur        
    def insert(self, val):
        node = Node(val)
        if not self.root:
            self.root = node
        else:
            leaf = self.traverse(self.root, val)
            if val < leaf.val:
                leaf.left = node
            else:
                leaf.right = node
    def sumAtDepth(self, depth):
        curDepth = 0
        # Initial function didn't include this check; when
        # asked, I added a @checkForRoot decorator to the
        # function, then wrote it directly into the function
        # to show what it would do.
        if not self.root:
            raise Exception("No tree!")
        nodes = {0:[self.root]}
        while curDepth <= depth:
            nodes[curDepth+1] = []
            for node in nodes[curDepth]:
                if node.left:
                    nodes[curDepth+1].append(node.left)
                if node.right:
                    nodes[curDepth+1].append(node.right)
            curDepth += 1        
        return sum([x.val for x in nodes[depth]])        

class Node:
    left = None
    right = None
    val = None
    def __init__(self, val):
        self.val = val

# The interviewer pointed out that the above is broken, because
# left and right and val are class variables. Things I learn in an
# interview! With more research and talking to a friend, I realize
# that I write all of my Python poorly; the above should be this 
# instead  The same applies to the BST classes above; root shouldn't
# be defined as a class variable, and should instead be defined 
# inside init.

# This still leaves me wondering how the heck you're meant to document
# instance variables in Python in a readable way; I like the documentation
# of things like:
# https://github.com/openlayers/openlayers/blob/master/lib/OpenLayers/Filter/Comparison.js
# And don't know how to get that in Python.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
