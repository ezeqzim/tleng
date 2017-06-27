import ply.yacc as yacc
from .lexer import tokens

# enable_debug = True
enable_debug = False

# E -> Z
def p_expression_zero(p):
  'expression : ZERO'
  if (enable_debug):
    print 'zero'
  p[0] = p[1]

# E -> B
def p_expression_boolean(p):
  'expression : boolean'
  if (enable_debug):
    print 'boolean'
  p[0] = p[1]

# E -> var
def p_expression_var(p):
  'expression : VAR'
  if (enable_debug):
    print 'var'
  p[0] = p[1]

# E -> (E)
def p_expression_brackets(p):
  'expression : OPENBRACKET expression CLOSEDBRACKET'
  if (enable_debug):
    print 'brackets'
  p[0] = p[2]

# E -> succ(E)
def p_expression_succ(p):
  'expression : SUCC OPENBRACKET expression CLOSEDBRACKET'
  if (enable_debug):
    print 'succ'
  p[0] = p[3] + 1

# E -> pred(E)
def p_expression_pred(p):
  'expression : PRED OPENBRACKET expression CLOSEDBRACKET'
  if (enable_debug):
    print 'pred'
  p[0] = p[3] - 1 if (p[3] > 0) else p[3]

# E -> iszero(E)
def p_expression_iszero(p):
  'expression : ISZERO OPENBRACKET expression CLOSEDBRACKET'
  if (enable_debug):
    print 'iszero'
  p[0] = p[3] == 0

# E -> if E then E else E
def p_expression_if_then_else(p):
  'expression : IF expression THEN expression ELSE expression'
  if (enable_debug):
    print 'if then else'
  p[0] = p[4] if p[2] else p[6]

# E -> L
def p_expression_abstraction(p):
  'expression : abstraction'
  if (enable_debug):
    print 'abs'
  p[0] = p[1]

# B -> true
def p_boolean_true(p):
  'boolean : TRUE'
  if (enable_debug):
    print 'true'
  p[0] = p[1]

# B -> false
def p_boolean_false(p):
  'boolean : FALSE'
  if (enable_debug):
    print 'false'
  p[0] = p[1]

# T -> Bool
def p_type_bool_maybe_arrow(p):
  'type : BOOL rectype'
  if (enable_debug):
    print 'bool'
  p[0] = p[1]

# T -> Nat
def p_type_nat_maybe_arrow(p):
  'type : NAT rectype'
  if (enable_debug):
    print 'nat'
  p[0] = p[1]

# T -> ->
def p_rectype_arrow_type(p):
  'rectype : ARROW type'
  if (enable_debug):
    print '->'
  p[0] = p[1] + p[2]

# T -> LAMBDA
def p_rectype_empty(p):
  'rectype : '
  if (enable_debug):
    print 'empty type'
  pass

# L -> \var:Type.E
def p_abstraction_lambda_maybe_application(p):
  'abstraction : LAMBDA VAR COLON type POINT expression application'
  if (enable_debug):
    print 'lambda'
  p[0] = p[6]

# A -> E
def p_application_expression(p):
  'application : expression'
  if (enable_debug):
    print 'app'
  p[0] = p[1]

# A -> LAMBDA
def p_application_lambda(p):
  'application : '
  if (enable_debug):
    print 'empty app'
  pass

def p_error(p):
  print("Hubo un error en el parseo.")
  parser.restart()

parser = yacc.yacc(debug=True)

def apply_parser(str):
  return parser.parse(str)
