grammar python_pd1;

// Simple Python-like grammar (subset) for assignments and expressions
program: statement+ EOF;

statement: assignment ;

assignment
    : VARIABLE ASSIGN expression
    | VARIABLE ADD_ASSIGN expression
    | VARIABLE SUB_ASSIGN expression
    | VARIABLE MUL_ASSIGN expression
    | VARIABLE DIV_ASSIGN expression
    ;

// expression with basic precedence (mul/div/mod > add/sub)
expression
    : expression MUL expression    # mulExpr
    | expression DIV expression    # divExpr
    | expression MOD expression    # modExpr
    | expression ADD expression    # addExpr
    | expression SUB expression    # subExpr
    | '(' expression ')'           # parenExpr
    | list                         # listExpr
    | STRING                       # stringExpr
    | NUMBER                       # numberExpr
    | VARIABLE                     # variableExpr
    ;

list: '[' (expression (COMMA expression)*)? ']';

// lexer tokens
ASSIGN     : '=' ;
ADD_ASSIGN : '+=' ;
SUB_ASSIGN : '-=' ;
MUL_ASSIGN : '*=' ;
DIV_ASSIGN : '/=' ;

ADD        : '+' ;
SUB        : '-' ;
MUL        : '*' ;
DIV        : '/' ;
MOD        : '%' ;
COMMA      : ',' ;

VARIABLE   : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER     : [0-9]+ ('.' [0-9]+)? ;
STRING     : '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'' ;

LINE_COMMENT: '#' ~[\r\n]* -> skip ;
WS : [ \t\r\n]+ -> skip ;