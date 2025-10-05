# python
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        if len(parts) == 1:
            new_nodes.append(node)
            continue

        if len(parts) % 2 == 0:
            raise Exception("Invalid markdown: unmatched delimiter")

        rebuilt = []
        for i, piece in enumerate(parts):
            if piece == "":
                continue
            if i % 2 == 0:
                rebuilt.append(TextNode(piece, TextType.TEXT))
            else:
                rebuilt.append(TextNode(piece, text_type))
        new_nodes.extend(rebuilt)
    return new_nodes