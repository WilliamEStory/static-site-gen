import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "some paragraph text", {"class": "text"})
        self.assertEqual(node.to_html(), '<p class="text">some paragraph text</p>')
    
    def test_leaf_to_html_none(self):
        node = LeafNode(None, "some text")
        self.assertEqual(node.to_html(), "some text")
        
    def test_leaf_to_html_div_no_props(self):
        node = LeafNode("div", "some text")
        self.assertEqual(node.to_html(), '<div>some text</div>')