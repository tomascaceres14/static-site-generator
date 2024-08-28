import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        htmlnode1 = HTMLNode("a", "test node", [], {"href": "google.com"})
        self.assertRaises(NotImplementedError, htmlnode1.to_html)

    def test_props_to_html(self):
        htmlnode1 = HTMLNode("a", "test node", [], {"href": "google.com"})
        self.assertEqual(htmlnode1.props_to_html(), ' href="google.com"')

    def test_to_html(self):
        node = LeafNode("a", "esto es un texto de prueba")
        node2 = LeafNode("a", "vamos a google", {"href": "google.com"})
        self.assertEqual(node.to_html(), "<a>esto es un texto de prueba</a>")
        self.assertEqual(node2.to_html(), '<a href="google.com">vamos a google</a>')

    def test_parent_basic(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            node.to_html(),
        )

    def test_parent_nested(self):
        child_node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        node = ParentNode(
            "div",
            [child_node],
        )

        self.assertEqual(
            "<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>",
            node.to_html(),
        )


if __name__ == "__main__":
    unittest.main()
