import ply.yacc as yacc
from .lexer import tokens

def p_root_expression(p):
  'root : expression'
  p[0] = p[1]

# Z
def p_expression_zero(p):
  'expression : zero'
  p[0] = p[1]

# B
def p_expression_boolean(p):
  'expression : boolean'
  p[0] = p[1]

# if E then E else E
def p_expression_if_then_else(p):
  'expression : IF expression THEN expression ELSE expression'
  p[0] = p[4] if p[2] else p[6]

# (E)
def p_expression_brackets(p):
  'expression : OPENBRACKET expression CLOSEDBRACKET'
  p[0] = p[2]

# var
def p_expression_var(p):
  'expression : VAR'
  p[0] = p[1]

# L
def p_expression_abstraction(p):
  'expression : abstraction'
  p[0] = p[1]

# A
def p_expression_application(p):
  'expression : application'
  p[0] = p[1]

# succ(E)
def p_expression_succ(p):
  'expression : SUCC OPENBRACKET expression CLOSEDBRACKET'
  p[0] = p[3] + 1

# pred(E)
def p_expression_pred(p):
  'expression : PRED OPENBRACKET expression CLOSEDBRACKET'
  p[0] = p[3] - 1 if (p[3] > 0) else p[3]

# iszero(E)
def p_expression_iszero(p):
  'expression : ISZERO OPENBRACKET expression CLOSEDBRACKET'
  p[0] = p[3] == 0

# 0
def p_zero_zero(p):
  'zero : ZERO'
  p[0] = p[1]

# true | false
def p_boolean_true(p):
  'boolean : TRUE'
  p[0] = p[1]

def p_boolean_false(p):
  'boolean : FALSE'
  p[0] = p[1]

# \var:Type.E
def p_abstraction_lambda(p):
  'abstraction : LAMBDA VAR COLON type POINT expression'
  p[0] = p[6]

# Bool
def p_type_bool(p):
  'type : BOOL'
  p[0] = p[1]

# Nat
def p_type_nat(p):
  'type : NAT'
  p[0] = p[1]

# ->
def p_type_arrow(p):
  'type : type ARROW type'
  p[0] = p[1] + p[2] + p[3]

def p_application_lambda_expression(p):
  'application : abstraction expression'
  p[0] = p[1](p[2])

def p_error(p):
  print("Hubo un error en el parseo.")
  parser.restart()

parser = yacc.yacc(debug=True)

def apply_parser(str):
  return parser.parse(str)
