from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value):
        if not isinstance(value, TextNode):
            return False
        
        return (
            self.text == value.text
            and self.text_type == value.text_type
            and self.url == value.url
        )

    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'
    
def text_node_to_html_node(text_node):
    tt = text_node.text_type

    if tt == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif tt == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif tt == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif tt == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif tt == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif tt == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
