import argparse
import sys
from pathlib import Path
from antlr4 import InputStream, CommonTokenStream
from python_pd1Lexer import python_pd1Lexer
from python_pd1Parser import python_pd1Parser
from antlr4.tree.Tree import TerminalNodeImpl
from main import print_tree


def parse_and_print(path: Path, pretty: bool = False):
    with path.open("r", encoding="utf-8") as f:
        data = f.read()

    input_stream = InputStream(data)
    lexer = python_pd1Lexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = python_pd1Parser(tokens)
    tree = parser.program()

    if pretty:
        print_tree(tree)
    else:
        print(tree.toStringTree(recog=parser))


def main():
    ap = argparse.ArgumentParser(description="Parse a sample Python-like file and print its parse tree.")
    ap.add_argument("file", nargs="?", default=Path(__file__).parent / "project_deliverable_1.py")
    ap.add_argument("--pretty", action="store_true", help="Print a human-friendly tree instead of toStringTree() output")
    args = ap.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(1)

    parse_and_print(path, pretty=args.pretty)


if __name__ == "__main__":
    main()
    