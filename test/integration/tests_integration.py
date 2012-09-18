#!/usr/bin/python

import unittest
from yampress import Yampress

class BasicUsageTest(unittest.TestCase):
    def setUp(self):
        self.sut = Yampress()

    def assertStartsWith(self, expected, current):
        self.assertTrue(current.startswith(expected), '\nexpected:\n{}\n---\ncurrent:{}\n---\n'.format(expected, current))

    def assertEndsWith(self, expected, current):
        self.assertTrue(current.endswith(expected), '\nexpected:\n{}\n---\ncurrent:{}\n---\n'.format(expected, current))

    def assertContains(self, expected, current):
        self.assertTrue(expected in current, '\nexpected:\n{}\n---\ncurrent:{}\n---\n'.format(expected, current))

    def test_setting_the_title(self):
        given = """---
title: this is the title
"""
        expected = "<!doctype html><html><head><title>this is the title</title></head>"

        current = self.sut.process(given)

        self.assertStartsWith(expected, current)

    def test_has_a_initial_page(self):
        given = """---
title: this is the title
"""
        expected = '<div id="impress"><div class="step slide" data-y="0"><h1>this is the title</h1></div></div>'
        current = self.sut.process(given)

        self.assertContains(expected, current)

    def test_footer(self):
        given = """---
title: this is the title
"""
        expected = '<script src="impress.js"></script><script>impress().init();</script></body></html>'
        current = self.sut.process(given)
        self.assertEndsWith(expected, current)

    def test_adding_styles(self):
        given = """---
title: this is the title
style: [style1.css, style2.css]
"""
        expected = '<link href="style1.css" rel="stylesheet"/><link href="style2.css" rel="stylesheet"/>'
        current = self.sut.process(given)

        self.assertContains(expected, current)

