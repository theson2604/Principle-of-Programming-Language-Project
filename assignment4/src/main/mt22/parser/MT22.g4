//2052450
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (variable_decl | function_declaration)+ EOF ;

//Comment
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;


//Statement
	// Statements
statement: if_else_stmt | other_stmt;
// match_stmt: IF LPARENT expr RPARENT match_stmt ELSE match_stmt
// 		  | other_stmt
// 		  ;
if_else_stmt: IF LPARENT expr RPARENT statement
			| IF LPARENT expr RPARENT statement ELSE statement
			;

other_stmt: assign_stmt
		 | for_stmt
		 | while_stmt
		 | do_while_stmt
		 | block_stat
		 | break_stmt
		 | continue_stmt
		 | return_stmt
		 | call_stmt
		 ;
	//Block statement
block_stat: LCURLY list_element RCURLY;
list_element: (statement | variable_decl)*;
	//Call statement
call_stmt: function_call SECOLON;
	//If-else statement
// if_else_stmt: IF LPARENT expr RPARENT statement (ELSE statement)?;
	//Do-while statement
do_while_stmt: DO block_stat WHILE LPARENT expr RPARENT SECOLON;
	//While statement
while_stmt: WHILE LPARENT expr RPARENT statement;
	//For statement
for_stmt: FOR LPARENT assign_ops (COMMA expr) (COMMA expr) RPARENT statement;
	//Assignment statement
assign_stmt: assign_ops SECOLON;
assign_ops: lhs EQASSIGN expr;
lhs: array_access | ID;
	//Break statement
break_stmt: BREAK SECOLON;
	//Continue statement
continue_stmt: CONTINUE SECOLON;
	//Return statement
return_stmt: RETURN expr? SECOLON;

//EXpression
// expr: array_access											#ExprArrayAccess
// 	| <assoc=right>MINUS  expr 							#Unary
// 	| <assoc=right>NOT  expr								#Unary
// 	| LPARENT expr RPARENT 									#Parenthesis
// 	| expr (MULT | DIV | MOD) expr 						#arithmetic
// 	| expr (PLUS | MINUS) expr 							#arithmetic
// 	| expr (AND | OR) expr 								#BinaryOp
// 	| expr (EQ | NEQ | LESS | LE | GREATER | GE) expr 	#Relational
// 	| expr CONCAT expr 									#Concat
// 	| boollit 											#Value
// 	| STRINGLIT 											#Value
// 	| FLOATLIT 											#Value
// 	| INTLIT 											#Value
// 	| ID													#ExprID
// 	| function_call											#ExprFuncCall
// 	;

// Expression
expr: relational_expr CONCAT relational_expr | relational_expr;
relational_expr: logical_expr (EQ | NEQ | LESS | LE | GREATER | GE) logical_expr | logical_expr;
logical_expr: logical_expr (AND | OR) adding_expr | adding_expr;
adding_expr: adding_expr (PLUS|MINUS) multiplying_expr | multiplying_expr;
multiplying_expr: multiplying_expr (MULT|DIV|MOD) unary_logical_expr | unary_logical_expr;
unary_logical_expr: NOT unary_logical_expr | unary_sign_expr;
unary_sign_expr: MINUS unary_sign_expr | parent_expr;
parent_expr: LPARENT expr RPARENT | operand;
operand: literal | array_access | function_call | ID;

index_operator: LBRACKET list_expr RBRACKET;
function_call: ID LPARENT (list_expr)? RPARENT;

//Array access
array_access: ID index_operator;

list_expr: expr next_expr;
next_expr: COMMA expr next_expr |;
//Declaration
	//Function
function_declaration: ID COLON FUNCTION return_type LPARENT list_parameter RPARENT (INHERIT ID)? block_stat;
	//Variable
		///Parameter
list_parameter: parameter next_parameter|;
next_parameter: COMMA parameter next_parameter|;
parameter: INHERIT? OUT? ID COLON var_type;
		///Variable
variable_decl: full_variable | variable;
full_variable: ID next_variable expr SECOLON;
next_variable: COMMA ID next_variable expr COMMA | COLON var_type EQASSIGN;

variable: idList COLON var_type SECOLON;

idList: ID next_id;
next_id: COMMA ID next_id|;

// assign_expr: EQASSIGN list_expr |;



//Type
	//
var_type: atomic_type | auto_type | array_type;
return_type: atomic_type | auto_type | void_type | array_type;
	//Atomic type
atomic_type: INTEGER | FLOAT | BOOL | STRING;
	//Array type
array_type: ARRAY LBRACKET list_integer RBRACKET OF atomic_type;
list_integer: INTLIT next_integerlit;
next_integerlit: COMMA INTLIT next_integerlit |;

	// oid type
void_type: VOID;
	//Auto type
auto_type: AUTO;


// Lexemes
	//Literals
literal: INTLIT | FLOATLIT | boollit | STRINGLIT | arraylit;
		//Array
arraylit: LCURLY array_elements RCURLY;
array_elements: element next_elements |;
next_elements: COMMA element next_elements |;
element: expr | arraylit;
		//Float
FLOATLIT: (INT DECIMAL EXP|INT DECIMAL|DECIMAL EXP|INT EXP) {self.text = self.text.replace('_','')};
fragment INT: DIGIT ('_'?FULL_DIGIT)* | [0];
fragment DECIMAL: DOT (FULL_DIGIT*)?;
fragment EXP: [eE][+-]? FULL_DIGIT+;
		//Integer
INTLIT: (DIGIT ('_'?FULL_DIGIT)* | [0]) {self.text = self.text.replace('_','')};
		//Boolean
boollit: TRUE|FALSE;
		//String
fragment ALLOW_CHAR: ~[\r\n\\'"] | ESCAPE_SEQUENCE;
UNCLOSE_STRING: '"' ALLOW_CHAR* {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: '"' ALLOW_CHAR* ('\\' ~([nrbft] | '\'')) {raise IllegalEscape(self.text[1:])};
STRINGLIT: UNCLOSE_STRING '"' {self.text = self.text[1:-1]};
	
	//Keywords
AUTO: 'auto';
BREAK: 'break';
BOOL: 'boolean';
DO: 'do';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNCTION: 'function';
IF: 'if';
INTEGER: 'integer';
RETURN: 'return';
STRING: 'string';
TRUE: 'true';
WHILE: 'while';
VOID: 'void';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';
ARRAY: 'array';

	//Operator
		//Arithmetic
PLUS: '+';
MULT: '*';
DIV: '/';
MOD: '%';
MINUS: '-';
		//Relational
NOT: '!';
AND: '&&';
OR: '||';
EQ: '==';
NEQ: '!=';
LESS: '<';
GREATER: '>';
LE: '<=';
GE: '>=';
		//String operator
CONCAT: '::';

	//Seperator
LPARENT: '(';
RPARENT: ')';
LBRACKET: '[';
RBRACKET: ']';
LCURLY: '{';
RCURLY: '}';
DOT: '.';
COMMA: ',';
COLON: ':';
SECOLON: ';';
EQASSIGN: '=';
	
// LIST_DIGIT: FULL_DIGIT (COMMA FULL_DIGIT)*;
	//Identifiers
ID: FULL_LETTER (FULL_LETTER|FULL_DIGIT)*;

	//Character set
fragment UPPER_LETTER: [A-Z];

fragment LOWER_LETTER: [a-z];

fragment FULL_LETTER: [A-Za-z_];

fragment DIGIT: [1-9];

fragment FULL_DIGIT: [0-9];

fragment ESCAPE_SEQUENCE: 
				 '\\\''
				|'\\"'
				|'\\\\'
				|'\\b'
				|'\\f'
				|'\\n'
				|'\\r'
				|'\\t'
				;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)};