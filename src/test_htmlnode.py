import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        n = HTMLNode(props=None)
        self.assertEqual(n.props_to_html(), "")

    def test_one_prop(self):
        n = HTMLNode(props={"href": "x"})
        self.assertEqual(n.props_to_html(), ' href="x"')
    
    def test_multiple_props(self):
        n = HTMLNode(props={"href": "x", "target": "_blank"})
        out = n.props_to_html()
        self.assertEqual(out.count('href="x"'), 1)
        self.assertEqual(out.count('target="_blank"'), 1)
        self.assertTrue(out.startswith(" "))
    
    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )
    
    def test_to_html_with_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()