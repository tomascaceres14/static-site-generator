import re
from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnotes, text_node_to_html_node

blocktype_paragraph = "paragraph"
blocktype_heading = "heading"
blocktype_code = "code"
blocktype_quote = "quote"
blocktype_unordered_list = "unordered_list"
blocktype_ordered_list = "ordered_list"


def markdown_to_blocks(markdown: str):
    return list(
        filter(
            lambda x: x != "", list(map(lambda x: x.strip(), markdown.split("\n\n")))
        )
    )


def block_to_block_type(md_block: str) -> str:
    regex = {
        "heading": r"^#{1,6} .+",
        "code": r"^```[\s\S]*?```$",
        "quote": r"^(> .*\n?)+",
    }

    block_split = md_block.split("\n")

    for line in block_split:
        if line.startswith("* ") or line.startswith("- "):
            return blocktype_unordered_list
        elif re.search(r"^\d+\.\s", line) != None:
            return blocktype_ordered_list

    for exp in regex:
        if re.search(regex[exp], md_block) is None:
            return blocktype_paragraph

        return exp


def text_to_children(text: str) -> list:
    text_nodes = text_to_textnotes(text)
    children = []

    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block: str):
    ParentNode("p", text_to_children(block.replace("\n", " ")))


def heading_to_html_node(block: str):
    text = " ".join(block.split("\n"))
    heading_level = text.split(" ")[0].count("#")
    LeafNode(f"h{heading_level}", text_to_children(text))


def code_to_html_node(block: str):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")

    text = block[4:-3]
    code = ParentNode("code", text_to_children(text))
    return ParentNode("pre", [code])


def quote_to_html_node(block: str):
    lines = block.split("\n")
    childrens = []
    for line in lines:
        childrens.append(text_to_children(line))

    return ParentNode("blockquote", childrens)


def markdown_to_html_node(markdown: str):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)

    ParentNode("div", children)


def block_to_html_node(block: str):
    block_type = block_to_block_type(block)

    if block_type == blocktype_paragraph:
        return paragraph_to_html_node(block)
    if block_type == blocktype_heading:
        return heading_to_html_node(block)
    if block_type == blocktype_quote:
        return quote_to_html_node(block)


if __name__ == "__main__":
    md_text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""

    blocks = markdown_to_blocks(md_text)
    print(block_to_block_type(blocks[2]))
