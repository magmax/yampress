#!/usr/bin/python

# Copyright (C) 2012 Miguel Angel Garcia <miguelangel.garcia@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
        self.body = ''


class Document(object):
    def __init__(self):
        self.header = None
        self.cover = None
        self.slides = []


class Impress(object):
    TMPL_MAIN = '<!doctype html>\n<html>\n<head>{header}\n</head>\n<body>\n'\
        '<div id="impress">\n<div id="cover">{cover}\n</div>{body}\n</div>\n<script src="impress.js">'\
        '</script>\n<script>impress().init();</script>\n</body>\n</html>'
    TMPL_PAGE_TITLE = '\n<title>{}</title>'
    TMPL_STYLE = '\n<link href="{}.css" rel="stylesheet"/>'
    TMPL_COVER_TITLE = '\n<h1>{}</h1>'
    TMPL_COVER_SLIDE = '\n<div class="step slide" data-y="{}">{}\n</div>'
    TMPL_TITLE = '\n<h1 class="title">{}</h1>'
    TMPL_SLIDE = '\n<div class="step slide" data-y="{}">{}{}\n</div>'
    TMPL_CONTENT_NORMAL = '\n<p>{}</p>'
    TMPL_CONTENT_LISTITEM = '\n<li>{}</li>'
    TMPL_CONTENT_LIST = '\n<ul>{}\n</ul>'

    def __init__(self):
        self.step = 800
        self.position = 0

    def render(self, document):
        content = {}
        content['header'] = self._render_header(document.header)
        content['cover'] = self._render_cover(document.cover)
        content['body'] = self._render_slides(document.slides)
        return self.TMPL_MAIN.format(**content)

    def _render_header(self, header):
        result = ''
        if header.title:
            result += self.TMPL_PAGE_TITLE.format(header.title)

        for style in header.styles:
            result += self.TMPL_STYLE.format(style)
        return result

    def _render_cover(self, cover):
        title = self.TMPL_COVER_TITLE.format(cover.title)
        result = self.TMPL_COVER_SLIDE.format(self.position, title)
        self.position += self.step
        return result

    def _render_slides(self, slides):
        result = ''
        for slide in slides:
            result += self._render_slide(slide)
        return result

    def _render_slide(self, slide):
        titlefmt = self.TMPL_TITLE.format(slide.title) if slide.title else ''
        bodyfmt = self._render_slide_content(slide.body)
        result = self.TMPL_SLIDE.format(self.position, titlefmt, bodyfmt)
        self.position += self.step
        return result

    def _render_slide_content(self, content):
        if not content:
            return ''

        if type(content) is str:
            return self.TMPL_CONTENT_NORMAL.format(content)

        if type(content) is list:
            result = ''
            for item in content:
                result += self.TMPL_CONTENT_LISTITEM.format(item)
            return self.TMPL_CONTENT_LIST.format(result)


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
    parser.add_argument('--source', dest='source', action='store',
                        required=True, type=file,
                        help='file to process')
    parser.add_argument('--output', dest='output', action='store',
                        required=True,
                        help='output file')

    args = parser.parse_args()

    yampress = Yampress()
    with file(args.output, 'w+') as fd:
        fd.write(yampress.process(args.source))


if __name__ == '__main__':
    main()
