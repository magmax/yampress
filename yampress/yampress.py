#!/usr/bin/python

import yaml

class Yampress(object):
    def __init__(self):
        self.step = 800
        self.position = 0
        self.config = {}

    def process(self, iml):
        generator = yaml.load_all(iml)
        content = {}
        self.config = generator.next()
        content['head'] = self._process_head()
        content['title'] = self._process_title()
        content['body'] = self._process_body(generator)
        return '<!doctype html><html><head>{head}</head><body><div id="impress">{title}{body}</div><script src="impress.js"></script><script>impress().init();</script></body></html>'.format(**content)

    def _process_head(self):
        result = ''
        if self.config.has_key('title'):
            result += '<title>{}</title>'.format(self.config['title'])
        if self.config.has_key('style'):
            styles = self.config['style']
            if type(styles) is not list:
                result += '<link href="{}" rel="stylesheet"/>'.format(styles)
            else:
                for style in self.config['style']:
                    result += '<link href="{}" rel="stylesheet"/>'.format(style)
        return result

    def _process_title(self):
        result = ''
        if self.config.has_key('title'):
            result += '<div class="step slide" data-y="{}"><h1>{}</h1></div>'.format(self.position, self.config['title'])
        return result

    def _process_body(self, data):
        result = ''
        return result
