#! /usr/bin/env python3

# Script from https://gist.github.com/jiffyclub/5015986
# This script turns Markdown into HTML using the Python markdown library and wraps the result in a 
# complete HTML document with default Bootstrap styling so that it's immediately printable. 
# Requires the python libraries jinja2, markdown, and mdx_smartypants.
import argparse
import sys

import jinja2
import markdown

# To install dependencies in a virtualenv:
#     $ py -3 -3 venv .venv
#     $ .venv/Scripts/activate
#     $ pip install jinja2
#     $ pip install markdown
#
# To install dependencies on Ubuntu:
#     $ sudo apt-get install python-jinja2 python-markdown
TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <link href="http://netdna.bootstrapcdn.com/twitter-bootstrap/2.3.0/css/bootstrap-combined.min.css" rel="stylesheet">
    <style>
        body {
            font-family: sans-serif;
        }
        code, pre {
            font-family: monospace;
        }
        h1 code,
        h2 code,
        h3 code,
        h4 code,
        h5 code,
        h6 code {
            font-size: inherit;
        }
    </style>
</head>
<body>
<div class="container">
{{content}}
</div>
</body>
</html>
"""
# TEMPLATE = """<!DOCTYPE html>
# <html>
# <head>
#     <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
#     <meta name="referrer" content="no-referrer" />
#     <meta name="referrer" content="unsafe-url" />
#     <meta name="referrer" content="origin" />
#     <meta name="referrer" content="no-referrer-when-downgrade" />
#     <meta name="referrer" content="origin-when-cross-origin" />
#     <title>Page Title</title>
#     <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
#     <style>
#         body {
#             font-family: Helvetica,Arial,sans-serif;
#         }
#         code, pre {
#             font-family: monospace;
#         }
#     </style>
# </head>
# <body>
# <div class="container">
# {{content}}
# </div>
# </body>
# </html>
# """

def parse_args(args=None):
    d = 'Make a complete, styled HTML document from a Markdown file.'
    parser = argparse.ArgumentParser(description=d)
    parser.add_argument('mdfile', type=argparse.FileType('r'), nargs='?',
                        default=sys.stdin,
                        help='File to convert. Defaults to stdin.')
    parser.add_argument('-o', '--out', type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='Output file name. Defaults to stdout.')
    return parser.parse_args(args)


def main(args=None):
    args = parse_args(args)
    md = args.mdfile.read()
    extensions = ['extra', 'smarty']
    html = markdown.markdown(md, extensions=extensions, output_format='html5')
    doc = jinja2.Template(TEMPLATE).render(content=html)
    args.out.write(doc)


if __name__ == '__main__':
    sys.exit(main())