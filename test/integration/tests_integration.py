#!/usr/bin/python

import unittest
from yampress import Yampress

class BasicUsageTest(unittest.TestCase):
    def setUp(self):
        self.sut = Yampress()


    def test_setting_the_title(self):
        given = """---
title: this is the title
---
"""

        expected = """<!doctype html><html><head><title>this is the title</title></head>"""
        current = self.sut.process(given)
        self.assertTrue(current.startswith(expected), '\nexpected:\n{}\n---\ncurrent:{}\n---\n'.format(expected, current))
