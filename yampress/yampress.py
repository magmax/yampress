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
            result += self._get_slide(self.config['title'])
        return result

    def _process_body(self, data):
        result = ''
        for slide in data:
            if type(slide) is str:
                result += self._get_slide('', slide)
            elif type(slide) is dict:
                result += self._get_slide(slide.get('title', ''), slide.get('content', ''))
        return result

    def _get_styles(self):
        if not self.config.has_key('style'):
            return ''

        styles = self.config['style']
        if type(styles) is not list:
            return '<link href="{}" rel="stylesheet"/>'.format(styles)

        result = ''
        for style in styles:
            result += '<link href="{}" rel="stylesheet"/>'.format(style)
        return result

    def _get_slide(self, title, body=None):
        titlefmt = '<h1>{}</h1>'.format(title) if title else ''
        bodyfmt = '<p>{}</p>'.format(body) if body else ''
        result = '<div class="step slide" data-y="{}">{}{}</div>'.format(self.position, titlefmt, bodyfmt)
        self.position += self.step
        return result
