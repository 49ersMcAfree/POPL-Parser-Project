# Generated from python_pd3.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .python_pd3Parser import python_pd3Parser
else:
    from python_pd3Parser import python_pd3Parser

# This class defines a complete listener for a parse tree produced by python_pd3Parser.
class python_pd3Listener(ParseTreeListener):

    # Enter a parse tree produced by python_pd3Parser#program.
    def enterProgram(self, ctx:python_pd3Parser.ProgramContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#program.
    def exitProgram(self, ctx:python_pd3Parser.ProgramContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#statement.
    def enterStatement(self, ctx:python_pd3Parser.StatementContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#statement.
    def exitStatement(self, ctx:python_pd3Parser.StatementContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#assignment.
    def enterAssignment(self, ctx:python_pd3Parser.AssignmentContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#assignment.
    def exitAssignment(self, ctx:python_pd3Parser.AssignmentContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#ifStatement.
    def enterIfStatement(self, ctx:python_pd3Parser.IfStatementContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#ifStatement.
    def exitIfStatement(self, ctx:python_pd3Parser.IfStatementContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#whileStatement.
    def enterWhileStatement(self, ctx:python_pd3Parser.WhileStatementContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#whileStatement.
    def exitWhileStatement(self, ctx:python_pd3Parser.WhileStatementContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#forStatement.
    def enterForStatement(self, ctx:python_pd3Parser.ForStatementContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#forStatement.
    def exitForStatement(self, ctx:python_pd3Parser.ForStatementContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#block.
    def enterBlock(self, ctx:python_pd3Parser.BlockContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#block.
    def exitBlock(self, ctx:python_pd3Parser.BlockContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#expression.
    def enterExpression(self, ctx:python_pd3Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#expression.
    def exitExpression(self, ctx:python_pd3Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#orExpr.
    def enterOrExpr(self, ctx:python_pd3Parser.OrExprContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#orExpr.
    def exitOrExpr(self, ctx:python_pd3Parser.OrExprContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#andExpr.
    def enterAndExpr(self, ctx:python_pd3Parser.AndExprContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#andExpr.
    def exitAndExpr(self, ctx:python_pd3Parser.AndExprContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#notExpr.
    def enterNotExpr(self, ctx:python_pd3Parser.NotExprContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#notExpr.
    def exitNotExpr(self, ctx:python_pd3Parser.NotExprContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#comparison.
    def enterComparison(self, ctx:python_pd3Parser.ComparisonContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#comparison.
    def exitComparison(self, ctx:python_pd3Parser.ComparisonContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#arithExpr.
    def enterArithExpr(self, ctx:python_pd3Parser.ArithExprContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#arithExpr.
    def exitArithExpr(self, ctx:python_pd3Parser.ArithExprContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#term.
    def enterTerm(self, ctx:python_pd3Parser.TermContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#term.
    def exitTerm(self, ctx:python_pd3Parser.TermContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#parenExpr.
    def enterParenExpr(self, ctx:python_pd3Parser.ParenExprContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#parenExpr.
    def exitParenExpr(self, ctx:python_pd3Parser.ParenExprContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#unaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:python_pd3Parser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:python_pd3Parser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#listExpr.
    def enterListExpr(self, ctx:python_pd3Parser.ListExprContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#listExpr.
    def exitListExpr(self, ctx:python_pd3Parser.ListExprContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#stringExpr.
    def enterStringExpr(self, ctx:python_pd3Parser.StringExprContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#stringExpr.
    def exitStringExpr(self, ctx:python_pd3Parser.StringExprContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#numberExpr.
    def enterNumberExpr(self, ctx:python_pd3Parser.NumberExprContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#numberExpr.
    def exitNumberExpr(self, ctx:python_pd3Parser.NumberExprContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#trueExpr.
    def enterTrueExpr(self, ctx:python_pd3Parser.TrueExprContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#trueExpr.
    def exitTrueExpr(self, ctx:python_pd3Parser.TrueExprContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#falseExpr.
    def enterFalseExpr(self, ctx:python_pd3Parser.FalseExprContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#falseExpr.
    def exitFalseExpr(self, ctx:python_pd3Parser.FalseExprContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#variableExpr.
    def enterVariableExpr(self, ctx:python_pd3Parser.VariableExprContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#variableExpr.
    def exitVariableExpr(self, ctx:python_pd3Parser.VariableExprContext):
        pass


    # Enter a parse tree produced by python_pd3Parser#list.
    def enterList(self, ctx:python_pd3Parser.ListContext):
        pass

    # Exit a parse tree produced by python_pd3Parser#list.
    def exitList(self, ctx:python_pd3Parser.ListContext):
        pass



del python_pd3Parser