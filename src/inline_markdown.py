from htmlnode import LeafNode
from textnode import TextNode, textnode_types
import re


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

        splitted_node = node.text.split(delimiter)

        for i in range(len(splitted_node)):

            if splitted_node[i] == "":
                continue

            if i % 2 == 0:
                new_nodes.append(
                    TextNode(splitted_node[i], textnode_types["text_type_text"])
                )
            else:
                new_nodes.append(TextNode(splitted_node[i], text_type))

    return new_nodes


def extract_markdown_images(text: str) -> list[tuple]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> list[tuple]:
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:

    new_nodes = []

    for node in old_nodes:

        if node.text == "":
            continue

        tuples_list = extract_markdown_images(node.text)

        if not tuples_list:
            new_nodes.append(node)
            continue

        for t in tuples_list:

            image_name = t[0]
            image_url = t[1]

            splitted = node.text.split(f"![{image_name}]({image_url})", 1)
            new_nodes.append(TextNode(splitted[0], textnode_types["text_type_text"]))
            new_nodes.append(
                TextNode(image_name, textnode_types["text_type_image"], image_url)
            )

            node.text = node.text.replace(
                f"{splitted[0]}![{image_name}]({image_url})", ""
            )
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:

    new_nodes = []

    for node in old_nodes:

        if node.text == "":
            continue

        tuples_list = extract_markdown_links(node.text)

        if not tuples_list:
            new_nodes.append(node)
            continue

        for t in tuples_list:

            link_text = t[0]
            href = t[1]

            splitted = node.text.split(f"[{link_text}]({href})", 1)
            new_nodes.append(TextNode(splitted[0], textnode_types["text_type_text"]))
            new_nodes.append(
                TextNode(link_text, textnode_types["text_type_link"], href)
            )

            node.text = node.text.replace(f"{splitted[0]}[{link_text}]({href})", "")
    return new_nodes


def text_to_textnotes(text: str):
    nodes = [TextNode(text, textnode_types["text_type_text"])]
    nodes = split_nodes_delimiter(nodes, "**", textnode_types["text_type_bold"])
    nodes = split_nodes_delimiter(nodes, "*", textnode_types["text_type_italic"])
    nodes = split_nodes_delimiter(nodes, "`", textnode_types["text_type_code"])
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


if __name__ == "__main__":
    txt = "This is **bold** text with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print(text_to_textnotes(txt))
