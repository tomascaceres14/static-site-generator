from textnode import TextNode

def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node2)
    print(node == node2)


main()