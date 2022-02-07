import random
from collections import deque


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        self.next = None
        self.parent = None
        self.count = None


def are_identical(root1, root2):
    if root1 == None and root2 == None:
        return True

    if root1 != None and root2 != None:
        return (root1.data == root2.data and
                are_identical(root1.left, root2.left) and
                are_identical(root1.right, root2.right))

    return False


class InorderIterator:
  def __init__(self, root):
    self.stack = [root]
    node = root.left
    while node:
      self.stack.append(node)
      node = node.left


  def hasNext(self):
    return True if self.stack else False

  # getNext returns null if there are no more elements in tree
  def getNext(self):
    if not self.stack:
      return None
    node = self.stack.pop()
    side = node.right
    while side:
      self.stack.append(side)
      side = side.left
    return node

def inorder_using_iterator(root):
  iter = InorderIterator(root)
  result = ""
  while iter.hasNext():
    ptr = iter.getNext()
    result += str(ptr.data) + " "
  return result