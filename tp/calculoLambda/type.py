from .types import *

class Type(object):
  def printString(self):
    return str(self.type)

class Bool(Type):
  def __init__(self, value):
    self.type = Types.BOOL

class Nat(Type):
  def __init__(self, value):
    self.type = Types.NAT

class Arrow(Type):
  def __init__(self, left, right = None):
    self.left = left
    self.right = right
    self.type = left.type if right is None else Types.ARROW

  def printString(self):
    if (self.type == Types.ARROW):
      return self.left.printString() + ' -> ' + self.right.printString()
    return self.left.printString()
