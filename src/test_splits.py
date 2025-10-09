import unittest
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType

class TestSplits(unittest.TestCase):
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
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://imgur.com/zjjcJKZ.com) and another [second link](https://imgur.com/3elNhQu.com)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://imgur.com/zjjcJKZ.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://imgur.com/3elNhQu.com"),
            ],
            new_nodes,
        )
    
    def test_split_links_no_link(self):
        node = TextNode(
            "This is text with no links.",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with no links.", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_split_links_only_links(self):
        node = TextNode(
            "[link](https://imgur.com/zjjcJKZ.com)[second link](https://imgur.com/3elNhQu.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://imgur.com/zjjcJKZ.com"),
                TextNode("second link", TextType.LINK, "https://imgur.com/3elNhQu.com"),
            ],
            new_nodes,
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes,
        )