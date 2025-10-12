from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    counter = 0
    for i in block:
        if i == "#":
            counter += 1
        else:
            break
    if len(block) > counter + 1 and block[counter] == ' ' and 1 <= counter <= 6:
        return BlockType.HEADING
    
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    if all(line.startswith(">") for line in block.splitlines()):
        return BlockType.QUOTE
    
    lines = block.splitlines()
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    
    if all(line.startswith(f"{i + 1}. ") for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    res = []
    new_markdown = markdown.split("\n\n")
    for i in new_markdown:
        i = i.strip()
        if len(i) != 0:
            res.append(i)
    return res
