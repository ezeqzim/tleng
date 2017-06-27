#! coding: utf-8
import ply.lex as lex

reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'Bool' : 'BOOL',
   'Nat' : 'NAT',
   'succ' : 'SUCC',
   'pred' : 'PRED',
   'iszero' : 'ISZERO',
   'true' : 'TRUE',
   'false' : 'FALSE',
}

tokens = [
  'VAR',
  'LAMBDA',
  'COLON',
  'POINT',
  'ZERO',
  'OPENBRACKET',
  'CLOSEDBRACKET',
  'ARROW'
] + list(reserved.values())

t_VAR = r'[a-z][a-zA-Z]*'
t_LAMBDA = r'\\'
t_COLON = r':'
t_POINT = r'\.'
t_OPENBRACKET = r'\('
t_CLOSEDBRACKET = r'\)'
t_ARROW = r'->'

t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'
t_BOOL = r'Bool'
t_NAT = r'Nat'
t_SUCC = r'succ'
t_PRED = r'pred'
t_ISZERO = r'iszero'

t_ignore = ' \t'

def t_ZERO(t):
  r'0'
  t.value = 0
  return t

def t_TRUE(t):
  r'true'
  t.value = True
  return t

def t_FALSE(t):
  r'false'
  t.value = False
  return t

lexer = lex.lex()

def apply_lexer(string):
  lexer.input(string)
  return list(lexer)
