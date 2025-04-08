import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("div", "value", None, {"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), " class=\"container\" id=\"main\"")
        
    def test_props_to_html_none(self):
        node = HTMLNode("div", "value", None, {})
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_single(self):
        node = HTMLNode("div", "value", None, {"class": "container"})
        self.assertEqual(node.props_to_html(), " class=\"container\"")