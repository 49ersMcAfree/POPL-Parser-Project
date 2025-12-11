import sys
from antlr4 import *
from python_pd3Lexer import python_pd3Lexer
from python_pd3Parser import python_pd3Parser

def main():
    # use filename from command line, or default to deliverable_3.py
    input_file = sys.argv[1] if len(sys.argv) > 1 else "deliverable_3.py"

    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = python_pd3Lexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = python_pd3Parser(tokens)

    tree = parser.program()   # start rule
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main()# D3 Runner
