# python
from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

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

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        extracted_markdown = extract_markdown_images(node.text)
        current_text = node.text
        if not extracted_markdown:
                new_nodes.append(TextNode(node.text, TextType.TEXT))
                continue
        for i in extracted_markdown:
            image_alt = i[0]
            image_link = i[1]
            parts = current_text.split(f"![{image_alt}]({image_link})", 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            current_text = parts[1]
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        extracted_markdown = extract_markdown_links(node.text)
        current_text = node.text
        if not extracted_markdown:
                new_nodes.append(TextNode(node.text, TextType.TEXT))
                continue
        for i in extracted_markdown:
            alt = i[0]
            link = i[1]
            parts = current_text.split(f"[{alt}]({link})", 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, link))
            current_text = parts[1]
        if current_text:
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    bold = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    image = split_nodes_image(code)
    link = split_nodes_link(image)
    return link