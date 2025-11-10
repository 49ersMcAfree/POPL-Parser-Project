# Generated from pd1\python_pd1.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,20,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,35,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,3,3,46,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,5,3,63,8,3,10,3,12,3,66,9,3,1,4,1,4,1,4,1,4,5,4,72,8,
        4,10,4,12,4,75,9,4,3,4,77,8,4,1,4,1,4,1,4,0,1,6,5,0,2,4,6,8,0,0,
        91,0,11,1,0,0,0,2,17,1,0,0,0,4,34,1,0,0,0,6,45,1,0,0,0,8,67,1,0,
        0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,
        1,0,0,0,14,15,1,0,0,0,15,16,5,0,0,1,16,1,1,0,0,0,17,18,3,4,2,0,18,
        3,1,0,0,0,19,20,5,16,0,0,20,21,5,5,0,0,21,35,3,6,3,0,22,23,5,16,
        0,0,23,24,5,6,0,0,24,35,3,6,3,0,25,26,5,16,0,0,26,27,5,7,0,0,27,
        35,3,6,3,0,28,29,5,16,0,0,29,30,5,8,0,0,30,35,3,6,3,0,31,32,5,16,
        0,0,32,33,5,9,0,0,33,35,3,6,3,0,34,19,1,0,0,0,34,22,1,0,0,0,34,25,
        1,0,0,0,34,28,1,0,0,0,34,31,1,0,0,0,35,5,1,0,0,0,36,37,6,3,-1,0,
        37,38,5,1,0,0,38,39,3,6,3,0,39,40,5,2,0,0,40,46,1,0,0,0,41,46,3,
        8,4,0,42,46,5,18,0,0,43,46,5,17,0,0,44,46,5,16,0,0,45,36,1,0,0,0,
        45,41,1,0,0,0,45,42,1,0,0,0,45,43,1,0,0,0,45,44,1,0,0,0,46,64,1,
        0,0,0,47,48,10,10,0,0,48,49,5,12,0,0,49,63,3,6,3,11,50,51,10,9,0,
        0,51,52,5,13,0,0,52,63,3,6,3,10,53,54,10,8,0,0,54,55,5,14,0,0,55,
        63,3,6,3,9,56,57,10,7,0,0,57,58,5,10,0,0,58,63,3,6,3,8,59,60,10,
        6,0,0,60,61,5,11,0,0,61,63,3,6,3,7,62,47,1,0,0,0,62,50,1,0,0,0,62,
        53,1,0,0,0,62,56,1,0,0,0,62,59,1,0,0,0,63,66,1,0,0,0,64,62,1,0,0,
        0,64,65,1,0,0,0,65,7,1,0,0,0,66,64,1,0,0,0,67,76,5,3,0,0,68,73,3,
        6,3,0,69,70,5,15,0,0,70,72,3,6,3,0,71,69,1,0,0,0,72,75,1,0,0,0,73,
        71,1,0,0,0,73,74,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,76,68,1,0,0,
        0,76,77,1,0,0,0,77,78,1,0,0,0,78,79,5,4,0,0,79,9,1,0,0,0,7,13,34,
        45,62,64,73,76
    ]

class python_pd1Parser ( Parser ):

    grammarFileName = "python_pd1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "']'", "'='", "'+='", 
                     "'-='", "'*='", "'/='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                      "MUL_ASSIGN", "DIV_ASSIGN", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "COMMA", "VARIABLE", "NUMBER", "STRING", "LINE_COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_expression = 3
    RULE_list = 4

    ruleNames =  [ "program", "statement", "assignment", "expression", "list" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ASSIGN=5
    ADD_ASSIGN=6
    SUB_ASSIGN=7
    MUL_ASSIGN=8
    DIV_ASSIGN=9
    ADD=10
    SUB=11
    MUL=12
    DIV=13
    MOD=14
    COMMA=15
    VARIABLE=16
    NUMBER=17
    STRING=18
    LINE_COMMENT=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(python_pd1Parser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_pd1Parser.StatementContext)
            else:
                return self.getTypedRuleContext(python_pd1Parser.StatementContext,i)


        def getRuleIndex(self):
            return python_pd1Parser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = python_pd1Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.statement()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==16):
                    break

            self.state = 15
            self.match(python_pd1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(python_pd1Parser.AssignmentContext,0)


        def getRuleIndex(self):
            return python_pd1Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = python_pd1Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(python_pd1Parser.VARIABLE, 0)

        def ASSIGN(self):
            return self.getToken(python_pd1Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,0)


        def ADD_ASSIGN(self):
            return self.getToken(python_pd1Parser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(python_pd1Parser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(python_pd1Parser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(python_pd1Parser.DIV_ASSIGN, 0)

        def getRuleIndex(self):
            return python_pd1Parser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = python_pd1Parser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(python_pd1Parser.VARIABLE)
                self.state = 20
                self.match(python_pd1Parser.ASSIGN)
                self.state = 21
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.match(python_pd1Parser.VARIABLE)
                self.state = 23
                self.match(python_pd1Parser.ADD_ASSIGN)
                self.state = 24
                self.expression(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(python_pd1Parser.VARIABLE)
                self.state = 26
                self.match(python_pd1Parser.SUB_ASSIGN)
                self.state = 27
                self.expression(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.match(python_pd1Parser.VARIABLE)
                self.state = 29
                self.match(python_pd1Parser.MUL_ASSIGN)
                self.state = 30
                self.expression(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.match(python_pd1Parser.VARIABLE)
                self.state = 32
                self.match(python_pd1Parser.DIV_ASSIGN)
                self.state = 33
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return python_pd1Parser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StringExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(python_pd1Parser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)


    class VariableExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(python_pd1Parser.VARIABLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableExpr" ):
                listener.enterVariableExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableExpr" ):
                listener.exitVariableExpr(self)


    class ModExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_pd1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,i)

        def MOD(self):
            return self.getToken(python_pd1Parser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModExpr" ):
                listener.enterModExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModExpr" ):
                listener.exitModExpr(self)


    class AddExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_pd1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(python_pd1Parser.ADD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)


    class NumberExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(python_pd1Parser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)


    class MulExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_pd1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(python_pd1Parser.MUL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)


    class DivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_pd1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,i)

        def DIV(self):
            return self.getToken(python_pd1Parser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivExpr" ):
                listener.enterDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivExpr" ):
                listener.exitDivExpr(self)


    class SubExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_pd1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,i)

        def SUB(self):
            return self.getToken(python_pd1Parser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubExpr" ):
                listener.enterSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubExpr" ):
                listener.exitSubExpr(self)


    class ListExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_(self):
            return self.getTypedRuleContext(python_pd1Parser.ListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListExpr" ):
                listener.enterListExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListExpr" ):
                listener.exitListExpr(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a python_pd1Parser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = python_pd1Parser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = python_pd1Parser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 37
                self.match(python_pd1Parser.T__0)
                self.state = 38
                self.expression(0)
                self.state = 39
                self.match(python_pd1Parser.T__1)
                pass
            elif token in [3]:
                localctx = python_pd1Parser.ListExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.list_()
                pass
            elif token in [18]:
                localctx = python_pd1Parser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.match(python_pd1Parser.STRING)
                pass
            elif token in [17]:
                localctx = python_pd1Parser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.match(python_pd1Parser.NUMBER)
                pass
            elif token in [16]:
                localctx = python_pd1Parser.VariableExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(python_pd1Parser.VARIABLE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 62
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = python_pd1Parser.MulExprContext(self, python_pd1Parser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 47
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 48
                        self.match(python_pd1Parser.MUL)
                        self.state = 49
                        self.expression(11)
                        pass

                    elif la_ == 2:
                        localctx = python_pd1Parser.DivExprContext(self, python_pd1Parser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 50
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 51
                        self.match(python_pd1Parser.DIV)
                        self.state = 52
                        self.expression(10)
                        pass

                    elif la_ == 3:
                        localctx = python_pd1Parser.ModExprContext(self, python_pd1Parser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 53
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 54
                        self.match(python_pd1Parser.MOD)
                        self.state = 55
                        self.expression(9)
                        pass

                    elif la_ == 4:
                        localctx = python_pd1Parser.AddExprContext(self, python_pd1Parser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 56
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 57
                        self.match(python_pd1Parser.ADD)
                        self.state = 58
                        self.expression(8)
                        pass

                    elif la_ == 5:
                        localctx = python_pd1Parser.SubExprContext(self, python_pd1Parser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 59
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 60
                        self.match(python_pd1Parser.SUB)
                        self.state = 61
                        self.expression(7)
                        pass

             
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(python_pd1Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(python_pd1Parser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(python_pd1Parser.COMMA)
            else:
                return self.getToken(python_pd1Parser.COMMA, i)

        def getRuleIndex(self):
            return python_pd1Parser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)




    def list_(self):

        localctx = python_pd1Parser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(python_pd1Parser.T__2)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 458762) != 0:
                self.state = 68
                self.expression(0)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==15:
                    self.state = 69
                    self.match(python_pd1Parser.COMMA)
                    self.state = 70
                    self.expression(0)
                    self.state = 75
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 78
            self.match(python_pd1Parser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         




