grammar python_pd2;

// ----------------- PARSER RULES -----------------

program
    : (NEWLINE | statement NEWLINE+)* EOF
    ;

statement
    : assignment
    | ifStatement
    ;

assignment
    : VARIABLE ASSIGN expression
    | VARIABLE ADD_ASSIGN expression
    | VARIABLE SUB_ASSIGN expression
    | VARIABLE MUL_ASSIGN expression
    | VARIABLE DIV_ASSIGN expression
    ;

// ----------- expressions with booleans -----------

expression
    : orExpr
    ;

orExpr
    : andExpr (OR andExpr)*
    ;

andExpr
    : notExpr (AND notExpr)*
    ;

notExpr
    : NOT notExpr
    | compareExpr
    ;

compareExpr
    : addExpr ((LT | LTE | GT | GTE | EQ | NEQ) addExpr)?
    ;

addExpr
    : mulExpr ((ADD | SUB) mulExpr)*
    ;

mulExpr
    : unaryExpr ((MUL | DIV | MOD) unaryExpr)*
    ;

unaryExpr
    : ADD unaryExpr
    | SUB unaryExpr
    | primary
    ;

primary
    : '(' expression ')'
    | list
    | STRING
    | NUMBER
    | TRUE
    | FALSE
    | VARIABLE
    ;

list
    : '[' (expression (COMMA expression)*)? ']'
    ;

// ------------- if / elif / else -----------------

// single-line bodies, like:
//   if x < 5: y = 3
ifStatement
    : IF expression COLON statement
      (NEWLINE+ ELIF expression COLON statement)*
      (NEWLINE+ ELSE COLON statement)?
    ;

// ----------------- LEXER RULES ------------------

// assignment ops
ASSIGN     : '=' ;
ADD_ASSIGN : '+=' ;
SUB_ASSIGN : '-=' ;
MUL_ASSIGN : '*=' ;
DIV_ASSIGN : '/=' ;

// arithmetic
ADD        : '+' ;
SUB        : '-' ;
MUL        : '*' ;
DIV        : '/' ;
MOD        : '%' ;
COMMA      : ',' ;

// comparisons
LT         : '<' ;
LTE        : '<=' ;
GT         : '>' ;
GTE        : '>=' ;
EQ         : '==' ;
NEQ        : '!=' ;

// keywords / booleans / control flow
TRUE       : 'True' ;
FALSE      : 'False' ;
IF         : 'if' ;
ELIF       : 'elif' ;
ELSE       : 'else' ;
AND        : 'and' ;
OR         : 'or' ;
NOT        : 'not' ;

// identifiers / literals
VARIABLE   : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER     : [0-9]+ ('.' [0-9]+)? ;
STRING     : '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'' ;

COLON      : ':' ;

// comments / whitespace
LINE_COMMENT: '#' ~[\r\n]* -> skip ;
NEWLINE    : '\r'? '\n' ;
WS         : [ \t\r]+ -> skip ;
