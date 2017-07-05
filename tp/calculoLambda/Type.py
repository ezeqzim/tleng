from .Types import *

class Bool(object):
  def __init__(self):
    self.type = Types.BOOL

  def __eq__(self, other):
    if (isinstance(other, self.__class__)):
      return self.type == other.type

  def __ne__(self, other):
    return not self.__eq__(self, other)

  def evaluate(self):
    return self

  def printString(self):
    return 'Bool'

  def printType(self):
    return 'Bool'

class Nat(object):
  def __init__(self):
    self.type = Types.NAT

  def __eq__(self, other):
    if (isinstance(other, self.__class__)):
      return self.type == other.type

  def __ne__(self, other):
    return not self.__eq__(self, other)

  def evaluate(self):
    return self

  def printString(self):
    return 'Nat'

  def printType(self):
    return 'Nat'

class Arrow(object):
  def __init__(self, left, right = None):
    self.left = left
    self.right = right

  def __eq__(self, other):
    if (isinstance(other, self.__class__)):
      if (self.right is not None and other.right is not None):
        return self.left == other.left and self.right == other.right
      if (self.right is None and other.right is None):
        return self.left == other.left
    return False

  def __ne__(self, other):
    return not self.__eq__(self, other)

  def evaluate(self):
    if (self.right is None):
      return self.left
    return Arrow(self.left, self.right.evaluate())

  def printString(self):
    if (self.right is None):
      return self.left.printString()
    return self.left.printString() + ' -> ' + self.right.printString()

  def printType(self):
    if (self.right is None):
      return self.left.printType()
    return self.left.printType() + ' -> ' + self.right.printType()
