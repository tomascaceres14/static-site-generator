import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "esto es un texto de prueba")
        node2 = LeafNode("a", "vamos a google", {"href": "google.com"})
        self.assertEqual(node.to_html(), "<a>esto es un texto de prueba</a>")
        self.assertEqual(node2.to_html(), '<a href="google.com">vamos a google</a>')


if __name__ == "__main__":
    unittest.main()
