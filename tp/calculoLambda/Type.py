from .Types import *

class Bool(object):
  def __init__(self):
    self.type = Types.BOOL

  def __eq__(self, other):
    if (isinstance(other, self.__class__)):
      return self.getType() == other.getType()
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
      return self.getType() == other.getType()
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
  def __init__(self, param, result):
    self.param = param
    self.result = result

  def __eq__(self, other):
    if (isinstance(other, self.__class__)):
      return self.getParam() == other.getParam() and self.getResult() == other.getResult()
    return False

  def __ne__(self, other):
    return not self.__eq__(other)

  def getParam(self):
    return self.param

  def getResult(self):
    return self.result

  def printString(self):
    if (self.getResult() is None):
      return self.getParam().printString()
    return '(' + self.getParam().printString() + ' -> ' + self.getResult().printString() + ')'

  def printType(self):
    if (self.getResult() is None):
      return self.getParam().printType()
    return '(' + self.getParam().printType() + ' -> ' + self.getResult().printType() + ')'
