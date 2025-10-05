import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitDelimeter(unittest.TestCase):
    def test_no_text_type(self):
        nodes = [TextNode("a `b` c", TextType.TEXT)]
        out = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(len(out), 3)
        self.assertEqual(out[0].text, "a ")
        self.assertEqual(out[0].text_type, TextType.TEXT)
        self.assertEqual(out[1].text, "b")
        self.assertEqual(out[1].text_type, TextType.CODE)
    
    def test_unmatched_raises(self):
        nodes = [TextNode("a `b c", TextType.TEXT)]
        with self.assertRaises(Exception):
            split_nodes_delimiter(nodes, "`", TextType.CODE)