
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'TRUE FALSE IF THEN ELSE LAMBDA COLON POINT ZERO SUCC PRED ISZERO OPENBRACKET CLOSEDBRACKET TBOOL TNAT TARROWexpression : ZEROexpression : TRUEexpression : FALSEexpression : SUCC OPENBRACKET expression CLOSEDBRACKETexpression : PRED OPENBRACKET expression CLOSEDBRACKETexpression : ISZERO OPENBRACKET expression CLOSEDBRACKETexpression : IF expression THEN expression ELSE expression'
    
_lr_action_items = {'THEN':([1,4,7,11,17,18,20,22,],[-3,-1,-2,15,-4,-6,-5,-7,]),'FALSE':([0,6,9,10,12,15,21,],[1,1,1,1,1,1,1,]),'OPENBRACKET':([3,5,8,],[9,10,12,]),'PRED':([0,6,9,10,12,15,21,],[8,8,8,8,8,8,8,]),'ZERO':([0,6,9,10,12,15,21,],[4,4,4,4,4,4,4,]),'ELSE':([1,4,7,17,18,19,20,22,],[-3,-1,-2,-4,-6,21,-5,-7,]),'SUCC':([0,6,9,10,12,15,21,],[3,3,3,3,3,3,3,]),'CLOSEDBRACKET':([1,4,7,13,14,16,17,18,20,22,],[-3,-1,-2,17,18,20,-4,-6,-5,-7,]),'ISZERO':([0,6,9,10,12,15,21,],[5,5,5,5,5,5,5,]),'$end':([1,2,4,7,17,18,20,22,],[-3,0,-1,-2,-4,-6,-5,-7,]),'TRUE':([0,6,9,10,12,15,21,],[7,7,7,7,7,7,7,]),'IF':([0,6,9,10,12,15,21,],[6,6,6,6,6,6,6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,6,9,10,12,15,21,],[2,11,13,14,16,19,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> ZERO','expression',1,'p_expression_zero','parser.py',17),
  ('expression -> TRUE','expression',1,'p_expression_true','parser.py',21),
  ('expression -> FALSE','expression',1,'p_expression_false','parser.py',25),
  ('expression -> SUCC OPENBRACKET expression CLOSEDBRACKET','expression',4,'p_expression_succ','parser.py',29),
  ('expression -> PRED OPENBRACKET expression CLOSEDBRACKET','expression',4,'p_expression_pred','parser.py',33),
  ('expression -> ISZERO OPENBRACKET expression CLOSEDBRACKET','expression',4,'p_expression_iszero','parser.py',37),
  ('expression -> IF expression THEN expression ELSE expression','expression',6,'p_expression_if_then_else','parser.py',41),
]
