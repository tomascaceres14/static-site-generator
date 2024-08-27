class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        
        if self.props is None:
            return ""
        
        html_props = ''
        
        for prop in self.props:
            html_props += f' {prop}="{self.props[prop]}"'
        
        return html_props

    def __repr__(self) -> str:
        return f"{self.tag} \n {self.value} \n {self.children} \n {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None) -> None:
        super().__init__(tag, value, [], props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        
        if self.tag == None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode: {self.tag} \n {self.value} \n {self.props}"
    
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None) -> None:
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")

        if self.children is None:
            raise ValueError("Invalid HTML: no childrens")

        childrens = ''
        
        for child in self.children:
            childrens += f'{child.to_html()}'
        
        return f'<{self.tag}>{childrens}</{self.tag}>'