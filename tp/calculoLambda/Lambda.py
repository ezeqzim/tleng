from .Asserts import *
from .Type import *
from .Types import *
import copy

class Lambda(object):
  def __init__(self, var, vtype, body):
    var.setType(vtype)
    self.var = var
    self.vtype = vtype
    self.body = body
    self.type = Arrow(removeLastNone(vtype), body.getType())
    self.context = { var.getValue(): vtype }

  def getType(self):
    return self.type

  def getVar(self):
    return self.var

  def evaluate(self, context):
    auxContext = copy.deepcopy(context)
    auxContext.update(self.context)
    assertNotHasFreeVariables(self.body, auxContext)
    self.body = self.body.evaluate(auxContext)
    self.type.right = self.body.getType()
    return self

  def printString(self):
    return '\\' + self.var.printString() + ':' + self.vtype.printString() + '.' + self.body.printString()

  def printType(self):
    return self.type.printType()

  def findAndReplace(self, var, parameter):
    self.body = self.body.findAndReplace(var, parameter)
    return self

  def hasFreeVariables(self, context):
    auxContext = copy.deepcopy(context)
    auxContext.update(self.context)
    return self.body.hasFreeVariables(auxContext)

  def evalWith(self, parameter, context):
    self.context.pop(self.var.getValue())
    auxContext = copy.deepcopy(context)
    auxContext.update(self.context)
    self.body = self.body.findAndReplace(self.var, parameter).evaluate(auxContext)
    return self.body

def removeLastNone(vtype):
  if (vtype.right is None):
    return vtype.left
  return Arrow(vtype.left, removeLastNone(vtype.right))
