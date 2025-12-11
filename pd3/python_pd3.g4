grammar python_pd3;

// ------------- PARSER RULES -------------

program
    : NEWLINE* (statement NEWLINE*)* EOF
    ;

statement
    : assignment
    | ifStatement
    | whileStatement          // D3: while loop statement
    | forStatement            // D3: for loop statement
    ;

// ---------- assignments ----------

assignment
    : VARIABLE ASSIGN expression
    | VARIABLE ADD_ASSIGN expression
    | VARIABLE SUB_ASSIGN expression
    | VARIABLE MUL_ASSIGN expression
    | VARIABLE DIV_ASSIGN expression
    ;

// ---------- if / elif / else ----------

ifStatement
    : IF expression ':' block
      (ELIF expression ':' block)*
      (ELSE ':' block)?
    ;

// ---------- while loop (D3) ----------

whileStatement
    : WHILE expression ':' block     // D3: while loop syntax
    ;

// ---------- for loop (D3) ----------

forStatement
    : FOR VARIABLE IN expression ':' block                      // D3: for x in iterable
    | FOR VARIABLE IN RANGE '(' expression ')' ':' block        // D3: for x in range(stop)
    | FOR VARIABLE IN RANGE '(' expression ',' expression ')' ':' block      // D3: for x in range(start, stop)
    | FOR VARIABLE IN RANGE '(' expression ',' expression ',' expression ')' ':' block  // D3: for x in range(start, stop, step)
    ;

// simple blocks (no INDENT/DEDENT):
//   if cond: x = 1
//   if cond:
//       x = 1
//       y = 2
//   while cond:
//       x = x + 1
//       y = y - 1
//   for i in list:
//       process(i)
block
    : statement                # singleLineBlock
    | NEWLINE+ statement+      # multiLineBlock
    ;

// ---------- expressions with conditionals ----------

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
    | comparison
    ;

comparison
    : arithExpr ((LT | LTE | GT | GTE | EQ | NEQ) arithExpr)?
    ;

arithExpr
    : term ((ADD | SUB) term)*
    ;

term
    : factor ((MUL | DIV | MOD) factor)*
    ;

factor
    : '(' expression ')'      # parenExpr
    | list                    # listExpr
    | STRING                  # stringExpr
    | NUMBER                  # numberExpr
    | TRUE                    # trueExpr
    | FALSE                   # falseExpr
    | VARIABLE                # variableExpr
    ;

list
    : '[' (expression (COMMA expression)*)? ']'
    ;

// ------------- LEXER RULES -------------

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

IF         : 'if' ;
ELIF       : 'elif' ;
ELSE       : 'else' ;
WHILE      : 'while' ;      // D3: while keyword
FOR        : 'for' ;        // D3: for keyword
IN         : 'in' ;         // D3: in keyword
RANGE      : 'range' ;      // D3: range function keyword

AND        : 'and' ;
OR         : 'or' ;
NOT        : 'not' ;

TRUE       : 'True' ;
FALSE      : 'False' ;

LTE        : '<=' ;
GTE        : '>=' ;
EQ         : '==' ;
NEQ        : '!=' ;
LT         : '<' ;
GT         : '>' ;

VARIABLE   : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER     : [0-9]+ ('.' [0-9]+)? ;
STRING     : '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'' ;

LINE_COMMENT : '#' ~[\r\n]* -> skip ;  // D3: Comments already supported (same as pd2)
NEWLINE      : '\r'? '\n' ;
WS           : [ \t\r]+ -> skip ;