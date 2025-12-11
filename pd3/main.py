import sys
from antlr4 import InputStream, CommonTokenStream
from python_pd3Lexer import python_pd3Lexer
from python_pd3Parser import python_pd3Parser
from antlr4.tree.Tree import TerminalNodeImpl
from pathlib import Path


# I used these functions from a GitHub example to make the tree printing easier and cleaner.
# See: https://github.com/parrt


def print_tree(node, indent=""):
    """Pretty-print an ANTLR parse tree node (recursive)."""
    
    #null check
    if node is None: 
        print(f"{indent}null")
        return
    
    if isinstance(node, TerminalNodeImpl):
        print(f"{indent}{node.getText()}")
        return

    rule_name = python_pd3Parser.ruleNames[node.getRuleIndex()]

    if rule_name == "program":
        print("Program")
        print(f"{indent}└── Statements")
        for child in node.getChildren():
            print_tree(child, indent + "    ")
    elif rule_name == "statement":
        print(f"{indent}├── Assignment")
        for child in node.getChildren():
            print_tree(child, indent + "│   ")
    elif rule_name == "assignment":
        if node.getChild(0) is None or node.getChild(1) is None or node.getChild(2) is None:
            print(f"{indent}Incomplete assignment")
            return
        variable = node.getChild(0).getText()
        operator = node.getChild(1).getText()
        print(f"{indent}├── Variable: {variable}")
        print(f"{indent}├── Operator: {operator}")
        print(f"{indent}└── Value:")
        print_tree(node.getChild(2), indent + "    ")
    elif rule_name == "ifStatement":
        print(f"{indent}├── If Statement")
        for child in node.getChildren():
            print_tree(child, indent + "│   ")
    elif rule_name == "whileStatement":
        print(f"{indent}├── While Statement")
        for child in node.getChildren():
            print_tree(child, indent + "│   ")
    elif rule_name == "forStatement":
        print(f"{indent}├── For Statement")
        for child in node.getChildren():
            print_tree(child, indent + "│   ")
    elif rule_name == "expression":
        if node.getChildCount() == 1:
            print(f"{indent}{node.getChild(0).getText()}")
        else:
            for child in node.getChildren():
                print_tree(child, indent + "    ")
    else:
        if node.getChildren(): #error check 
            for child in node.getChildren():
                print_tree(child, indent + "    ")


def main():
    # Resolve sample input relative to this file's directory
    sample = Path(__file__).resolve().parent / "project_deliverable_3.py"
    if not sample.exists():
        print(f"Sample file not found: {sample}")
        sys.exit(1)

    with sample.open("r", encoding="utf-8") as file:
        input_code = file.read()

    input_stream = InputStream(input_code)
    lexer = python_pd3Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = python_pd3Parser(token_stream)
    tree = parser.program()

    # Compact tree
    print(tree.toStringTree(recog=parser))

    print("\n\n")
    print_tree(tree)


if __name__ == "__main__":
    main()
