#!/usr/bin/env python3
# This file is in the public domain.

"""
Extract translations from a Jinja2 template, stripping leading newlines.

@author Florian Dold
"""

import re
import jinja2.ext


def normalize(message):
    message = message.strip()
    # collapse whitespaces (including newlines) into one space.
    message = re.sub("\s+", " ", message)
    return message


def babel_extract(fileobj, keywords, comment_tags, options):
    res = jinja2.ext.babel_extract(fileobj, keywords, comment_tags, options)
    for lineno, funcname, message, comments in res:
        message = normalize(message)
        yield lineno, funcname, message, comments


def wrap_gettext(f):
    """
    Call gettext with whitespace normalized.
    """
    def wrapper(message):
        message = normalize(message)
        return f(message)
    return wrapper
