import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        htmlnode1 = HTMLNode("a", "test node", [], {"href": "google.com"})
        self.assertRaises(NotImplementedError, htmlnode1.to_html)

    def test_props_to_html(self):
        htmlnode1 = HTMLNode("a", "test node", [], {"href": "google.com"})
        self.assertEqual(htmlnode1.props_to_html(), ' href="google.com"')


if __name__ == "__main__":
    unittest.main()
