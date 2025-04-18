class HTMLNode:
    def __init__(self=None, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        html_string = " "
        for key, value in self.props.items():
            html_string += f"{key}=\"{value}\" "
        return html_string.rstrip()
            
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"