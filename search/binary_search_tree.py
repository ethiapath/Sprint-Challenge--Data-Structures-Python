from collections import deque

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    stack = []
    stack.append(self)
    while len(stack):
      item = stack.pop()
      cb(item.value)
      if item.right:
        stack.append(item.right)
      if item.left:
        stack.append(item.left)
    '''
    cb(self.value)
    if self.left:
      self.left.depth_first_for_each(cb)
    if self.right:
      self.right.depth_first_for_each(cb)
    '''

  def breadth_first_for_each(self, cb):
    queue = []
    queue.insert(0, self)
    while len(queue):
      item = queue.pop()
      cb(item.value)
      if item.left:
        queue.insert(0, item.left)
      if item.right:
        queue.insert(0, item.right)
    '''
    cb(self.value)
    if self.left:
      self.left.breadth_first_for_each(cb)
    if self.right:
      self.right.breadth_first_for_each(cb)
    '''

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)
    else:
      if not self.right:
        return False
      else:
        return self.right.contains(target)

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
