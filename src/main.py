from textnode import TextNode, TextType

def main():
    txtNode = TextNode(text="Hello, World!", text_type=TextType.NORMAL, url=None)
    print(txtNode)
    
main()