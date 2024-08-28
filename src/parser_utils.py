from htmlnode import LeafNode
from textnode import TextNode, textnode_types


def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type not in textnode_types.values():
        raise ValueError("Invalid text type")

    if text_node.text_type == textnode_types["text_type_text"]:
        return LeafNode(None, text_node.text).to_html()
    elif text_node.text_type == textnode_types["text_type_bold"]:
        return LeafNode("b", text_node.text).to_html()
    elif text_node.text_type == textnode_types["text_type_italic"]:
        return LeafNode("i", text_node.text).to_html()
    elif text_node.text_type == textnode_types["text_type_code"]:
        return LeafNode("code", text_node.text).to_html()
    elif text_node.text_type == textnode_types["text_type_link"]:
        return LeafNode("a", text_node.text, {"href": text_node.url}).to_html()
    elif text_node.text_type == textnode_types["text_type_image"]:
        return LeafNode(
            "img", "", {"src": text_node.url, "alt": text_node.text}
        ).to_html()


def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: str):

    new_nodes = []

    for node in old_nodes:
        if node.text_type != textnode_types["text_type_text"]:
            new_nodes.append(node)
            continue

        if delimiter not in node.text:
            raise ValueError("Delimiter not found")

        splitted_node = node.text.split(delimiter)

        new_nodes.append(TextNode(splitted_node[0], textnode_types["text_type_text"]))
        new_nodes.append(TextNode(splitted_node[1], text_type))
        new_nodes.append(TextNode(splitted_node[2], textnode_types["text_type_text"]))

    return new_nodes


if __name__ == "__main__":

    node = TextNode(
        "This is text with a **code block** word", textnode_types["text_type_text"]
    )
    new_nodes = split_nodes_delimiter([node], "**", textnode_types["text_type_bold"])
    print(new_nodes)
