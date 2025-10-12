import unittest
from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_block_to_block_type_heading(self):
        self.assertEqual(block_to_block_type("# Title"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Title"), BlockType.HEADING)
        self.assertNotEqual(block_to_block_type("####Title"), BlockType.HEADING)
        self.assertNotEqual(block_to_block_type("####### Title"), BlockType.HEADING)
        self.assertNotEqual(block_to_block_type("### "), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        self.assertEqual(block_to_block_type("```\ncode\n```"), BlockType.CODE)
        self.assertNotEqual(block_to_block_type("``code``"), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        self.assertEqual(block_to_block_type("> q"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("> a\n> b"), BlockType.QUOTE)

    def test_block_to_block_type_unordered(self):
        self.assertEqual(block_to_block_type("- a\n- b"), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered(self):
        self.assertEqual(block_to_block_type("1. a\n2. b\n3. c"), BlockType.ORDERED_LIST)