from .Types import *

class Bool(object):
  def __init__(self):
    self.type = Types.BOOL

  def __eq__(self, other):
    if (isinstance(other, self.__class__)):
      return self.getType() == other.type
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  def getType(self):
    return self.type

  def printString(self):
    return 'Bool'

  def printType(self):
    return 'Bool'

class Nat(object):
  def __init__(self):
    self.type = Types.NAT

  def __eq__(self, other):
    if (isinstance(other, self.__class__)):
      return self.getType() == other.type
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  def getType(self):
    return self.type

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
      if (self.getRight() is not None and other.getRight() is not None):
        return self.getLeft() == other.getLeft() and self.getRight() == other.getRight()
      if (self.getRight() is None and other.getRight() is None):
        return self.getLeft() == other.getLeft()
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  def getLeft(self):
    return self.left

  def getRight(self):
    return self.right

  def printString(self):
    if (self.getRight() is None):
      return self.getLeft().printString()
    return self.getLeft().printString() + ' -> ' + self.getRight().printString()

  def printType(self):
    if (self.getRight() is None):
      return self.getLeft().printType()
    return '(' + self.getLeft().printType() + ' -> ' + self.getRight().printType() + ')'
