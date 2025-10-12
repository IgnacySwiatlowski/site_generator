from textnode import TextNode, TextType
from copystatic import delete_contents, copy_recursive
import os

def main():
    node = TextNode("hello", TextType.TEXT)
    root = os.path.dirname(os.path.dirname(__file__))
    static_path = os.path.join(root, "static")
    public_path = os.path.join(root, "public")
    
    if not os.path.exists(public_path):
        os.mkdir(public_path)
    delete_contents(public_path)
    copy_recursive(static_path, public_path)

if __name__ == "__main__":
    main()