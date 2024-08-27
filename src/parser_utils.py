from htmlnode import LeafNode
from textnode import TextNode


def text_node_to_html_node(text_node: TextNode):
    textnode_types = {
        "text_type_text": "text",
        "text_type_bold": "bold",
        "text_type_italic": "italic",
        "text_type_code": "code",
        "text_type_link": "link",
        "text_type_image": "image",
    }

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
