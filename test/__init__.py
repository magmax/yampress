#!/usr/bin/python
# -*- coding:utf-8; tab-width:4; mode:python -*-

import os
import re
from jinja2 import Template, Environment

CURR_DIR = os.path.dirname(__file__)
JSON_FILE = os.path.join(CURR_DIR, 'tests.json')
TEST_FILE = os.path.join(CURR_DIR, 'auto_test.py')
TMPL_FILE = os.path.join(CURR_DIR, 'tests.template')


class Generator(object):
    def generate_tests(self):
        tests = self.get_tests()
        template = self.get_template()
        self.write_result(template.render(suites=tests))

    def get_tests(self):
        true = True
        with file(JSON_FILE) as fd:
            return eval(fd.read())

    def get_template(self):
        def substitute(r):
            r = re.sub('~', 'ntilde', r)
            r = re.sub('"', '\\"', r)
            r = re.sub('\W', '_', r)
            return r

        env = Environment()
        env.filters['validname'] = substitute
        with file(TMPL_FILE) as fd:
            template = env.from_string(fd.read())
        return template

    def write_result(self, content):
        with file(TEST_FILE, 'w+') as fd:
            fd.write(content)


if not os.path.exists(TEST_FILE) \
        or os.path.getmtime(TEST_FILE) < os.path.getmtime(JSON_FILE) \
        or os.path.getmtime(TEST_FILE) < os.path.getmtime(TMPL_FILE):
    print 'generating'
    gen = Generator()
    gen.generate_tests()
