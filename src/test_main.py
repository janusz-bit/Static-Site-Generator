import unittest

from main import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
)
from textnode import TextNode, TextType


class TestMarkdownExtraction(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfbeR92.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
                ("another", "https://i.imgur.com/dfbeR92.png"),
            ],
            matches,
        )

    def test_extract_markdown_images_none(self):
        text = "This is text with no images"
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.google.com) and [another](https://www.example.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("link", "https://www.google.com"),
                ("another", "https://www.example.com"),
            ],
            matches,
        )

    def test_extract_markdown_links_none(self):
        text = "This is text with no links"
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)

    def test_extract_markdown_links_not_images(self):
        text = "This is text with a ![image](https://example.com/image.png) and a [link](https://example.com/link)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("link", "https://example.com/link"),
            ],
            matches,
        )

    def test_extract_markdown_images_not_links(self):
        text = "This is text with a ![image](https://example.com/image.png) and a [link](https://example.com/link)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                ("image", "https://example.com/image.png"),
            ],
            matches,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.google.com) and [another](https://www.example.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.LINK, "https://www.example.com"),
            ],
            new_nodes,
        )

    def test_split_links_at_start(self):
        node = TextNode(
            "[link](https://www.google.com) is at the start",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" is at the start", TextType.TEXT),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
