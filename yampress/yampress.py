#!/usr/bin/python

import yaml

class Yampress(object):
    def process(self, iml):
        generator = yaml.load_all(iml)
        head = self._process_head(generator.next())
        body = self._process_body(generator)
        return '<!doctype html><html><head>{head}</head><body>{body}</body></html>'.format(head=head, body=body)

    def _process_head(self, data):
        result = ''
        if data.has_key('title'):
            result += '<title>{}</title>'.format(data['title'])
        return result

    def _process_body(self, data):
        result = ''
        return result
