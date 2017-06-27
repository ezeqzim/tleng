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

def t_ZERO(token):
  r'0'
  token.value = 0
  return token

def t_TRUE(token):
  r'true'
  token.value = True
  return token

def t_FALSE(token):
  r'false'
  token.value = False
  return token

def t_VAR(token):
  r'[a-z][a-zA-Z]*'
  if token.value in reserved:
    token.type = reserved[token.value]
    token.value = reserved[token.value]
  return token

lexer = lex.lex()

def apply_lexer(string):
  lexer.input(string)
  return list(lexer)
