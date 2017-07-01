import ply.yacc as yacc
from .lexer import tokens
from .expressions import *

# Aux -> Term
def p_aux_term(p):
  'aux : term'
  p[0] = Aux(p[1])

# Term -> App
def p_term_app(p):
  'term : app'
  p[0] = Application(p[1])

# Term -> succ(Term)
def p_term_succ_openbracket_term_closedbracket(p):
  'term : SUCC OPENBRACKET term CLOSEDBRACKET'
  p[0] = Succ(p[3])

# Term -> pred(Term)
def p_term_pred_openbracket_term_closedbracket(p):
  'term : PRED OPENBRACKET term CLOSEDBRACKET'
  p[0] = Pred(p[3])

# Term -> iszero(Term)
def p_term_iszero_openbracket_term_closedbracket(p):
  'term : ISZERO OPENBRACKET term CLOSEDBRACKET'
  p[0] = Iszero(p[3])

# Term -> if Term then Term else Term
def p_term_if_term_then_term_else_term(p):
  'term : IF term THEN term ELSE term'
  p[0] = IfThenElse(p[2], p[4], p[6])

# Term -> \var:T.Term
def p_term_lambda_var_colon_type_point_term(p):
  'term : LAMBDA VAR COLON type POINT term'
  p[0] = Abstraction(AVar(p[2]), p[4], p[6])

# Term -> (Term)
def p_term_openbracket_term_closedbracket(p):
  'term : OPENBRACKET term CLOSEDBRACKET'
  p[0] = Term(p[2])

# App -> ATerm
def p_app_aterm(p):
  'app : aterm'
  p[0] = App(p[1])

# App -> App ATerm
def p_app_app_aterm(p):
  'app : app aterm'
  p[0] = AppList(p[1], p[2])

# ATerm -> 0
def p_aterm_0(p):
  'aterm : ZERO'
  p[0] = AZero()

# ATerm -> true
def p_aterm_true(p):
  'aterm : TRUE'
  p[0] = ATrue()

# ATerm -> false
def p_aterm_false(p):
  'aterm : FALSE'
  p[0] = AFalse()

# ATerm -> var
def p_aterm_var(p):
  'aterm : VAR'
  p[0] = AVar(p[1])

# Type -> Bool Arrow
def p_type_bool_arrow(p):
  'type : BOOL arrow'
  p[0] = Arrow(Bool(p[1]), p[2])

# Type -> Nat Arrow
def p_type_nat_arrow(p):
  'type : NAT arrow'
  p[0] = Arrow(Nat(p[1]), p[2])

# Arrow -> -> Type
def p_arrow_arrow_type(p):
  'arrow : ARROW type'
  p[0] = Arrow(p[2])

# Arrow ->
def p_arrow(p):
  'arrow : '
  pass

def p_error(p):
  print 'Hubo un error en el parseo'
  parser.restart()

parser = yacc.yacc(debug=True)

def apply_parser(str):
  return parser.parse(str)
