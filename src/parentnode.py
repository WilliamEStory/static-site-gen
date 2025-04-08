from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag cannot be None for ParentNode")
        if not self.children:
            raise ValueError("Children cannot be None for ParentNode")
        
        html = f"<{self.tag}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html