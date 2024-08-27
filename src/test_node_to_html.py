import unittest

from parser_utils import text_node_to_html_node
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


if __name__ == "__main__":
    unittest.main()
