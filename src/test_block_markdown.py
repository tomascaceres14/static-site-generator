import unittest
from block_markdown import markdown_to_blocks, block_to_block_type


class TestBlockMarkdown(unittest.TestCase):
    def test_markdowns_to_blocks(self):
        md_text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""

        answer = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ]

        self.assertEqual(markdown_to_blocks(md_text), answer)

    def test_block_to_block_type(self):
        md_text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item

1. Hola que tal
2. Otro item
"""

        answer = ["heading", "paragraph", "unordered_list", "ordered_list"]

        blocks = markdown_to_blocks(md_text)
        self.assertEqual(block_to_block_type(blocks[0]), answer[0])
        self.assertEqual(block_to_block_type(blocks[1]), answer[1])
        self.assertEqual(block_to_block_type(blocks[2]), answer[2])
        self.assertEqual(block_to_block_type(blocks[3]), answer[3])


if __name__ == "__main__":
    unittest.main()
