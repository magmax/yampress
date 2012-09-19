#!/usr/bin/python

import yaml
import sys
import argparse

class Header(object):
    def __init__(self):
        self.title = None
        self.styles = []


class Cover(object):
    def __init__(self):
        self.title = None


class Slide(object):
    def __init__(self):
        self.title = ''


class Document(object):
    def __init__(self):
        self.header = None
        self.cover = None
        self.slides = []


class Impress(object):
    def __init__(self):
        self.step = 800
        self.position = 0

    def render(self, document):
        content = {}
        content['header'] = self._render_header(document.header)
        content['cover'] = self._render_cover(document.cover)
        content['body'] = self._render_slides(document.slides)
        return '<!doctype html>\n<html>\n<head>\n{header}</head>\n<body>\n<div id="impress">{cover}{body}</div>\n<script src="impress.js"></script>\n<script>impress().init();</script>\n</body>\n</html>'.format(**content)

    def _render_header(self, header):
        result = ''
        if header.title:
            result += '<title>{}</title>\n'.format(header.title)

        for style in header.styles:
            result += '<link href="{}" rel="stylesheet"/>\n'.format(style)
        return result

    def _render_cover(self, cover):
        result = ''
        titlefmt = '\n<h1>{}</h1>'.format(cover.title) if cover.title else ''
        result = '\n<div class="step slide" data-y="{}">{}\n</div>\n'.format(self.position, titlefmt)
        self.position += self.step
        return result

    def _render_slides(self, slides):
        result = ''
        for slide in slides:
            result += self._render_slide(slide)
        return result

    def _render_slide(self, slide):
        result = ''
        titlefmt = '\n<h1>{}</h1>'.format(slide.title) if slide.title else ''
        bodyfmt = '\n<p>{}</p>'.format(slide.body) if slide.body else ''
        result = '\n<div class="step slide" data-y="{}">{}{}\n</div>\n'.format(self.position, titlefmt, bodyfmt)
        self.position += self.step
        return result


class Yampress(object):
    def __init__(self):
        self.config = {}

    def process(self, iml):
        generator = yaml.load_all(iml)
        self.config = generator.next()

        renderer = Impress()
        return renderer.render(self._create_document(generator))

    def _create_document(self, data):
        document = Document()
        document.header = self._process_header()
        document.cover = self._process_cover()
        document.slides = self._process_slides(data)
        return document

    def _process_header(self):
        header = Header()
        header.title = self.config.get('title', '')

        styles = self.config.get('style', [])
        header.styles = styles if type(styles) is list else [styles]
        return header

    def _process_cover(self):
        cover = Cover()
        cover.title = self.config.get('title', '')
        return cover

    def _process_slides(self, data):
        slides = []
        for item in data:
            slide = Slide()
            slides.append(slide)
            if type(item) is str:
                slide.body = item
            elif type(item) is dict:
                slide.title = item.get('title', '')
                slide.body = item.get('content', '')
        return slides


def main():
    parser = argparse.ArgumentParser(description='Generate your pretty slides')
    parser.add_argument('--source', dest='source', action='store', required=True, type=file,
                        help='file to process')
    parser.add_argument('--output', dest='output', action='store', required=True,
                        help='output file')

    args = parser.parse_args()

    yampress = Yampress()
    with file(args.output, 'w+') as fd:
        fd.write(yampress.process(args.source))


if __name__ == '__main__':
    main()
