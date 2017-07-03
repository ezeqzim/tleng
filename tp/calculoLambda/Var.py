from .Types import *

class Var(object):
  def __init__(self, value):
    self.value = value
    self.type = Types.VAR
