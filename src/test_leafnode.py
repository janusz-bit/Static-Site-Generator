import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_basic(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://google.com"})
        self.assertEqual(node.to_html(), '<a href="https://google.com">Click me!</a>')

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_to_html_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_multiple_props(self):
        node = LeafNode(
            "a", "Click me!", {"href": "https://google.com", "target": "_blank"}
        )
        # Checking for space between properties
        self.assertEqual(
            node.to_html(), '<a href="https://google.com" target="_blank">Click me!</a>'
        )


if __name__ == "__main__":
    unittest.main()
