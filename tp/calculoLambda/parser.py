import ply.yacc as yacc
from .lexer import tokens

def p_expression_zero(p):
  'expression : ZERO'
  p[0] = p[1]

def p_expression_true(p):
  'expression : TRUE'
  p[0] = p[1]

def p_expression_false(p):
  'expression : FALSE'
  p[0] = p[1]

def p_expression_succ(p):
  'expression : SUCC OPENBRACKET expression CLOSEDBRACKET'
  p[0] = p[3] + 1

def p_expression_pred(p):
  'expression : PRED OPENBRACKET expression CLOSEDBRACKET'
  p[0] = p[3] - 1 if (p[3] > 0) else p[3]

def p_expression_iszero(p):
  'expression : ISZERO OPENBRACKET expression CLOSEDBRACKET'
  p[0] = p[3] == 0

def p_expression_if_then_else(p):
  'expression : IF expression THEN expression ELSE expression'
  p[0] = p[4] if p[2] else p[6]

def p_error(p):
  print("Hubo un error en el parseo.")
  parser.restart()

parser = yacc.yacc(debug=True)

def apply_parser(str):
  return parser.parse(str)
