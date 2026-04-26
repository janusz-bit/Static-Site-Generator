from enum import Enum

from leafnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.text, tag=None)
    if text_node.text_type == TextType.BOLD:
        return LeafNode(value=text_node.text, tag="b")
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(value=text_node.text, tag="i")
    if text_node.text_type == TextType.CODE:
        return LeafNode(value=text_node.text, tag="code")
    if text_node.text_type == TextType.LINK:
        return LeafNode(
            value=text_node.text, tag="a", props={"href": f"{text_node.url}"}
        )
    if text_node.text_type == TextType.IMAGE:
        return LeafNode(
            value="",
            tag="img",
            props={
                "src": f"{text_node.url}",
                "alt": f"{text_node.text}",
            },
        )
    raise ValueError(f"Invalid text type: {text_node.text_type}")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes
