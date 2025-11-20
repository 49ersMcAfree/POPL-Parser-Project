from pathlib import Path
import sys
from antlr4 import InputStream, CommonTokenStream
from python_pd2Lexer import python_pd2Lexer
from python_pd2Parser import python_pd2Parser
from antlr4.tree.Tree import TerminalNodeImpl

try:
    from PIL import Image, ImageDraw, ImageFont
except Exception:
    Image = ImageDraw = ImageFont = None


def build_lines(node, parser, indent=""):
    """Return a list of textual lines for the parse tree, using the provided format."""
    lines = []
    if isinstance(node, TerminalNodeImpl):
        lines.append(f"{indent}{node.getText()}")
        return lines

    rule_name = parser.ruleNames[node.getRuleIndex()]

    if rule_name == "program":
        lines.append("Program")
        lines.append(f"{indent}└── Statements")
        for child in node.getChildren():
            lines += build_lines(child, parser, indent + "    ")
    elif rule_name == "statement":
        lines.append(f"{indent}├── Assignment")
        for child in node.getChildren():
            lines += build_lines(child, parser, indent + "│   ")
    elif rule_name == "assignment":
        variable = node.getChild(0).getText()
        operator = node.getChild(1).getText()
        lines.append(f"{indent}├── Variable: {variable}")
        lines.append(f"{indent}├── Operator: {operator}")
        lines.append(f"{indent}└── Value:")
        lines += build_lines(node.getChild(2), parser, indent + "    ")
    elif rule_name == "expression":
        if node.getChildCount() == 1:
            lines.append(f"{indent}{node.getChild(0).getText()}")
        else:
            for child in node.getChildren():
                lines += build_lines(child, parser, indent + "    ")
    else:
        for child in node.getChildren():
            lines += build_lines(child, parser, indent + "    ")

    return lines


def save_lines_as_image(lines, out_path):
    if Image is None:
        print("Pillow not installed — cannot create image. Install with: pip install Pillow")
        return False

    font = ImageFont.load_default()
    padding = 8
    tmp_img = Image.new("RGB", (1, 1))
    tmp_draw = ImageDraw.Draw(tmp_img)
    maxw = 0
    line_h = 0
    for l in lines:
        bbox = tmp_draw.textbbox((0, 0), l, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        if w > maxw:
            maxw = w
        if h > line_h:
            line_h = h
    img_w = maxw + padding * 2
    img_h = line_h * len(lines) + padding * 2

    img = Image.new("RGB", (img_w, img_h), "white")
    draw = ImageDraw.Draw(img)
    y = padding
    for l in lines:
        draw.text((padding, y), l, fill="black", font=font)
        y += line_h

    img.save(out_path, format="JPEG")
    return True


def main():
    repo = Path(__file__).resolve().parent
    sample = repo / "project_deliverable_2.py"
    if not sample.exists():
        print(f"Sample not found: {sample}")
        return

    with sample.open("r", encoding="utf-8") as f:
        text = f.read()

    input_stream = InputStream(text)
    lexer = python_pd2Lexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = python_pd2Parser(tokens)
    tree = parser.program()

    # Build textual lines using the provided formatting logic
    lines = build_lines(tree, parser)

    # Print to stdout as fallback/verification
    print(tree.toStringTree(recog=parser))
    print("\n\n")
    for l in lines:
        print(l)

    # Save image
    out = repo / "parse_tree_from_main.jpg"
    if save_lines_as_image(lines, out):
        print(f"Saved parse tree image to: {out}")


if __name__ == '__main__':
    main()
from antlr4 import InputStream, CommonTokenStream
from python_pd2Lexer import python_pd2Lexer
from python_pd2Parser import python_pd2Parser
from antlr4.tree.Tree import TerminalNodeImpl
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def pretty_lines(node, parser, indent=""):
    lines = []
    from antlr4.tree.Tree import TerminalNodeImpl
    if isinstance(node, TerminalNodeImpl):
        lines.append(f"{indent}{node.getText()}")
        return lines

    rule_name = parser.ruleNames[node.getRuleIndex()]
    if rule_name == "program":
        lines.append("Program")
        lines.append(f"{indent}Statements")
        for child in node.getChildren():
            lines += pretty_lines(child, parser, indent + "    ")
    elif rule_name == "statement":
        for child in node.getChildren():
            lines += pretty_lines(child, parser, indent)
    elif rule_name == "assignment":
        variable = node.getChild(0).getText()
        operator = node.getChild(1).getText()
        lines.append(f"{indent}Assignment: {variable} {operator}")
        lines += pretty_lines(node.getChild(2), parser, indent + "    ")
    elif rule_name == "ifStatement":
        lines.append(f"{indent}If")
        for child in node.getChildren():
            lines += pretty_lines(child, parser, indent + "    ")
    else:
        if node.getChildCount() == 0:
            lines.append(f"{indent}{rule_name}")
        else:
            lines.append(f"{indent}{rule_name}")
            for child in node.getChildren():
                lines += pretty_lines(child, parser, indent + "    ")
    return lines


def main():
    repo = Path(__file__).resolve().parent
    sample = repo / "project_deliverable_2.py"
    if not sample.exists():
        print(f"Sample not found: {sample}")
        return

    with sample.open("r", encoding="utf-8") as f:
        text = f.read()

    input_stream = InputStream(text)
    lexer = python_pd2Lexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = python_pd2Parser(tokens)
    tree = parser.program()

    lines = pretty_lines(tree, parser)

    font = ImageFont.load_default()
    padding = 8
    tmp_img = Image.new("RGB", (1, 1))
    tmp_draw = ImageDraw.Draw(tmp_img)
    maxw = 0
    line_h = 0
    for l in lines:
        bbox = tmp_draw.textbbox((0, 0), l, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        if w > maxw:
            maxw = w
        if h > line_h:
            line_h = h
    img_w = maxw + padding * 2
    img_h = line_h * len(lines) + padding * 2

    img = Image.new("RGB", (img_w, img_h), "white")
    draw = ImageDraw.Draw(img)
    y = padding
    for l in lines:
        draw.text((padding, y), l, fill="black", font=font)
        y += line_h

    out = repo / "parse_tree.jpg"
    img.save(out, format="JPEG")
    print(f"Saved parse tree image to: {out}")


if __name__ == '__main__':
    main()
