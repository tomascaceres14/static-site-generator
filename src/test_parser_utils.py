import unittest

from parser_utils import text_node_to_html_node, split_nodes_delimiter
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


if __name__ == "__main__":
    unittest.main()
