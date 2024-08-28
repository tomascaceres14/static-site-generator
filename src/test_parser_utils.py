import unittest

from parser_utils import (
    text_node_to_html_node,
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
)
from textnode import TextNode


class TestNodeToHTML(unittest.TestCase):
    def test_node_to_html(self):

        nodes = [
            TextNode("testing text", "text"),
            TextNode("testing bold", "bold"),
            TextNode("testing italic", "italic"),
            TextNode("testing code", "code"),
            TextNode("testing image", "image", "imageurl.com"),
            TextNode("testing link", "link", "google.com"),
        ]

        solutions = [
            "testing text",
            "<b>testing bold</b>",
            "<i>testing italic</i>",
            "<code>testing code</code>",
            '<img src="imageurl.com" alt="testing image"></img>',
            '<a href="google.com">testing link</a>',
        ]

        for i in range(0, len(nodes)):
            self.assertEqual(text_node_to_html_node(nodes[i]), solutions[i])

        self.assertRaises(
            ValueError, text_node_to_html_node, TextNode("this is an error", "any")
        )

    def test_split_nodes_delimiter(self):

        test1 = TextNode("I am `testing` a funcitonality!", "text")
        solution1 = [
            TextNode("I am ", "text"),
            TextNode("testing", "code"),
            TextNode(" a funcitonality!", "text"),
        ]
        self.assertEqual(split_nodes_delimiter([test1], "`", "code"), solution1)

        test2 = [
            TextNode("I am **testing** a funcitonality!", "text"),
            TextNode("I am **testing** a funcitonality!", "bold"),
        ]
        solution2 = [
            TextNode("I am ", "text"),
            TextNode("testing", "bold"),
            TextNode(" a funcitonality!", "text"),
            TextNode("I am **testing** a funcitonality!", "bold"),
        ]
        self.assertEqual(split_nodes_delimiter(test2, "**", "bold"), solution2)

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        solution = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(extract_markdown_images(text), solution)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        solution = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(extract_markdown_links(text), solution)

    def test_split_nodes_image(self):
        node1 = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            "text",
        )

        solution1 = [
            TextNode(
                "This is text with a ",
                "text",
            ),
            TextNode("rick roll", "image", "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(
                " and ",
                "text",
            ),
            TextNode("obi wan", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]

        self.assertEqual(split_nodes_image([node1]), solution1)

        node2 = TextNode(
            "This is text without images",
            "text",
        )

        solution2 = [
            TextNode(
                "This is text without images",
                "text",
            )
        ]

        self.assertEqual(split_nodes_image([node2]), solution2)

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            "text",
        )

        solution = [
            TextNode("This is text with a link ", "text"),
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode(" and ", "text"),
            TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev"),
        ]

        self.assertEqual(split_nodes_link([node]), solution)


if __name__ == "__main__":
    unittest.main()
