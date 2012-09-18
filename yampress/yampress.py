#!/usr/bin/python

import yaml

class Yampress(object):
    def process(self, iml):
        generator = yaml.load_all(iml)
        content = {}
        config = generator.next()
        content['head'] = self._process_head(config)
        content['title'] = self._process_title(config)
        content['body'] = self._process_body(generator)
        return '<!doctype html><html><head>{head}</head><body><div id="impress">{title}{body}</div></body></html>'.format(**content)

    def _process_head(self, config):
        result = ''
        if config.has_key('title'):
            result += '<title>{}</title>'.format(config['title'])
        return result

    def _process_title(self, config):
        result = ''
        if config.has_key('title'):
            result += '<div class="step"><h1>{}</h1></div>'.format(config['title'])
        return result

    def _process_body(self, data):
        result = ''
        return result
