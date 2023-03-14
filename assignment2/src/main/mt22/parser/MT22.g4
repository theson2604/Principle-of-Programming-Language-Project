//ID: 2053399
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: declare+ EOF ;
// program: declare program | declare EOF ;
declare: var_declare | func_declare;

// 5.
//variable declaration

var_declare: ID nextID exp SEMI | id_list COLON types SEMI;
nextID: COMMA ID nextID exp COMMA | COLON types ASSIGN;
id_list: ID id_list2 | ID;
id_list2: COMMA ID id_list2 |;

// var_type: INTEGER|FLOAT|STRING|BOOLEAN|array_type|AUTO;
atomic_type: INTEGER|FLOAT|STRING|BOOLEAN;
array_type: ARRAY index_int OF atomic_type;

//function declaration
func_declare: func_proto (INHERIT ID)? func_body;
func_proto: ID COLON FUNCTION return_type params_list;
return_type: INTEGER|FLOAT|STRING|VOID|BOOLEAN|array_type|AUTO;
func_body: block_stmt;

param_declare: INHERIT? OUT? ID COLON types;
params_list: LP params RP;
params: param_declare params2 |;
params2: COMMA param_declare params2 |;
types: INTEGER|FLOAT|STRING|BOOLEAN|AUTO|array_type;

//6.
exp_bool: exp;
exp_int: exp;
exp_float: exp;
exp_string: exp;

exp: exp1 DC exp1 | exp1;
exp1: exp2 (EQ | NEQ | GT | LT | GTE | LTE) exp2 | exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | SUB) exp4 | exp4;
exp4: exp4 (MUL | DIV | MOD) exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: SUB exp6 | exp7;
exp7: exp7 index | operands;

operands: literals | ID | func_call | LP exp RP;

func_call: ID LP call_body RP;

//7.
stmt: assign_stmt | if_stmt | for_stmt | while_stmt | dowhile_stmt | break_stmt | continue_stmt | return_stmt | call_stmt | block_stmt;
// stmt_list: stmt stmt_list2 |;
// stmt_list2: stmt;

// assign_stmt: assign_lhs+ exp SEMI;
assign_stmt: lhs_list exp SEMI;
assign_lhs: scalar_var ASSIGN;
scalar_var: ID index?;
lhs_list: assign_lhs lhs_list2 | assign_lhs;
lhs_list2: assign_lhs lhs_list2 |;

if_stmt: IF LP exp_bool RP stmt (ELSE stmt)?;

for_stmt: FOR LP scalar_var ASSIGN exp COMMA exp_bool COMMA exp_int RP for_body;
for_body: stmt;

while_stmt: WHILE LP exp_bool RP while_body;
while_body: stmt;

dowhile_stmt: DO block_stmt WHILE LP exp_bool RP SEMI;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

return_stmt: RETURN (exp | func_call)? SEMI;

call_stmt: ID LP call_body RP SEMI;
call_body: exp call_body2 |;
call_body2: COMMA exp call_body2 |;

block_stmt: LCB block_body RCB ;
block_body: block_element block_body2 |;
block_body2: block_element block_body2 |;
block_element: stmt | var_declare;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
DC: '::';

AND: '&&';
OR: '||';
EQ: '==';
LTE: '<=';
GTE: '>=';
NEQ: '!=';
LT: '<' ;
GT: '>' ;

LP: '(';
RP: ')';
LCB: '{';
RCB: '}';
LSB: '[';
RSB: ']';
// EMT: '{}';

SEMI: ';';
COMMA: ',';
COLON: ':';
DOT: '.';
ASSIGN: '=';

// TRUE: 'true';
// FALSE: 'false';

INT: 'int';
INTEGER: 'integer';
FLOAT: 'float';
STRING: 'string';
BOOLEAN: 'boolean';
VOID: 'void';
ARRAY: 'array';

index_int: LSB list_int RSB;
list_int: INT_LIT list_int2 | INT_LIT;
list_int2: COMMA INT_LIT list_int2 |; 

index: LSB list_exp_int RSB;
list_exp_int: exp_int list_exp_int2 | exp_int;
list_exp_int2: COMMA exp_int list_exp_int2 |; 

INHERIT: 'inherit';
FUNCTION: 'function';
IF: 'if';
ELSE: 'else';
FOR: 'for';
WHILE: 'while';
DO: 'do';
BREAK: 'break';
CONTINUE: 'continue';
RETURN: 'return';
OUT: 'out';
AUTO: 'auto';
OF: 'of';

literals: FLOAT_LIT | INT_LIT | array_lit | STRING_LIT | BOOL_LIT;
// KEYWORDS: (AUTO|BREAK|BOOLEAN|DO|ELSE|FALSE|FLOAT|FOR|FUNCTION|IF|INTEGER|RETURN|STRING|TRUE|WHILE|VOID|OUT|CONTINUE|OF|INHERIT|ARRAY);
OPERATORS: ADD|SUB|MUL|DIV|MOD|NOT|AND|OR|EQ|LTE|GTE|NEQ|LT|GT;
SEPARATORS: LP|RP|LCB|RCB|LSB|RSB|SEMI|COMMA|COLON|DOT|ASSIGN;
BOOL_LIT: 'true'|'false';
STRING_LIT: DBQ STRING_CHAR* DBQ
	{
		y = str(self.text)
		self.text = y[1:-1]
	}
	;
FLOAT_LIT: ([1-9][0-9_]*|[0])? DEC EXP {self.text = self.text.replace('_', '')}| ([1-9][0-9_]*|[0]) DEC {self.text = self.text.replace('_', '')}| ([1-9][0-9_]*|[0]) EXP {self.text = self.text.replace('_', '')} ;
// FLOAT_LIT: ([1-9][0-9_]*|[0]) {self.text = self.text.replace('_', '')} (DEC EXP | DEC | EXP);
INT_LIT: ([1-9][0-9_]*|[0]) {self.text = self.text.replace('_', '')};
array_lit: LCB exp_list RCB ;
exp_list: exp exp_list2 |;
exp_list2: COMMA exp exp_list2 |;

ID: (CHARACTER|UNDERSCORE)(CHARACTER|DIGIT|UNDERSCORE)*;

fragment LOW_CHARACTER: [a-z];
fragment UP_CHARACTER: [A-Z];
fragment CHARACTER: (LOW_CHARACTER|UP_CHARACTER);
fragment DIGIT: [0-9];
fragment POS_DIGIT: [1-9];
fragment DEC: DOT DIGIT*;
fragment EXP: [eE][+-]?[0-9]+;
fragment UNDERSCORE: '_';
fragment DBQ: '"';

//Comment
BLOCK_COMMENT: ((DIV MUL) .*? (MUL DIV)) -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' STRING_CHAR* ( [\b\t\n\f\r"'\\] | EOF )
	{
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		if y[-1] == '"' and y[-2] == '\\': 
			raise UncloseString(y[1:])
		elif y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	}
	;


ILLEGAL_ESCAPE: '"' STRING_CHAR* EI
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;
fragment STRING_CHAR: ~[\b\t\n\f\r"'\\] | ES ;

fragment ES: '\\' [btnfr"'\\] | [\b\t\n\f\r];

fragment EI: '\\' ~[btnfr"'\\] | ~'\\' ;

ERROR_CHAR: . {raise ErrorToken(self.text)};