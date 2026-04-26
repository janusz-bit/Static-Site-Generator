import re

from textnode import TextNode, TextType


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:

    result = []
    for old_node in old_nodes:
        text = old_node.text
        images_tuples = extract_markdown_images(text)

        text_now = text
        for image_tuple in images_tuples:
            image = f"![{image_tuple[0]}]({image_tuple[1]})"
            half = text_now.split(image, 1)
            if half[0] != "":
                result.append(TextNode(half[0], TextType.TEXT))
            result.append(TextNode(image_tuple[0], TextType.IMAGE, image_tuple[1]))
            text_now = half[1]
        if text_now != "":
            result.append(TextNode(text_now, TextType.TEXT))
    return result


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:

    result = []
    for old_node in old_nodes:
        text = old_node.text
        link_tuples = extract_markdown_links(text)

        text_now = text
        for link_tuple in link_tuples:
            link = f"[{link_tuple[0]}]({link_tuple[1]})"
            half = text_now.split(link, 1)
            if half[0] != "":
                result.append(TextNode(half[0], TextType.TEXT))
            result.append(TextNode(link_tuple[0], TextType.LINK, link_tuple[1]))
            text_now = half[1]
        if text_now != "":
            result.append(TextNode(text_now, TextType.TEXT))

    return result


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)


if __name__ == "__main__":
    main()
