import unittest

from main import extract_markdown_images, extract_markdown_links


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


if __name__ == "__main__":
    unittest.main()
