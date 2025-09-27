from textnode import TextNode, TextType

def main():
    node = TextNode("hello", TextType.PLAIN_TEXT)
    print(node)

if __name__ == "__main__":
    main()