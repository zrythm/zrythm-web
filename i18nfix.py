#!/usr/bin/env python3
#
# This file is taken from the GNUnet project's website source code,
# originally in the public domain.
#
# This file is re-distributed under the terms of CC0 1.0 (Public Domain).
# You should have received a copy of CC0 1.0 along with this distribution.
# If not, see <https://creativecommons.org/publicdomain/zero/1.0/>.

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
