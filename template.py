#!/usr/bin/env python3
# coding: utf-8
# This file is in the public domain.
#
# This script runs the jinja2 templating engine on an input template-file
# using the specified locale for gettext translations, and outputs
# the resulting (HTML) ouptut-file.
#
# Note that the gettext files need to be prepared first. This script
# is thus to be invoked via the Makefile.
#
# We import unicode_literals until people have understood how unicode
# with bytes and strings changed in python2->python3.
from __future__ import unicode_literals
import os
import os.path
import sys
import re
import gettext
import glob
import codecs
import jinja2
import i18nfix

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                         extensions=["jinja2.ext.i18n"],
                         lstrip_blocks=True,
                         trim_blocks=True,
                         undefined=jinja2.StrictUndefined,
                         autoescape=False)
# DEBUG OUTPUT:
if (os.getenv("DEBUG")):
    print(sys.path)

langs_full = {
        "en": "English",
        "fr": "Français",
        "it": "Italiano",
        "es": "Español",
        "pt": "Português",
        "cs": "Czech",
        "de": "Deutsch",
        "pl": "Polski",
        "da": "Danish",
        "nl": "Nederlands",
        "et": "Eeti",
        "gd": "Gaelic",
        "el": "Ελληνικά",
        "nb_NO": "Bokmål",
        "fi": "Suomi",
        "sv": "Svenska",
        "ru": "русский",
        "ja": "日本語",
        "zh": "中文",
        "ko": "한국어",
        "ar": "العربية",
        "hi": "हिन्दी"}
lang_flags = {
        "en": "[en]",
        "fr": "[fr]",
        "it": "[it]",
        "es": "[es]",
        "pt": "[pt]",
        "cs": "[cs]",
        "de": "[de]",
        "pl": "[pl]",
        "da": "[da]",
        "nl": "[nl]",
        "et": "[et]",
        "gd": "[gd]",
        "el": "[el]",
        "nb_NO": "[nb]",
        "fi": "[fi]",
        "sv": "[sv]",
        "ru": "[ru]",
        "ja": "[ja]",
        "zh": "[zh]",
        "ko": "[ko]",
        "ar": "[ar]",
        "hi": "[hi]"}

for in_file in glob.glob("template/*.j2"):
    name, ext = re.match(r"(.*)\.([^.]+)$", in_file.rstrip(".j2")).groups()
    tmpl = env.get_template(in_file)

    def self_localized(other_locale):
        """
        Return URL for the current page in another locale.
        """
        return "../" + other_locale + "/" + in_file.replace('template/', '').rstrip(".j2")

    def url_localized(filename):
        return "../" + locale + "/" + filename

    def svg_localized(filename):
        lf = filename + "." + locale + ".svg"
        if locale == "en" or not os.path.isfile(lf):
            return "../" + filename + ".svg"
        else:
            return "../" + lf

    def url(x):
        # TODO: look at the app root environment variable
        # TODO: check if file exists
        return "../" + x

    for l in glob.glob("locale/*/"):
        locale = os.path.basename(l[:-1])

        tr = gettext.translation("messages",
                                 localedir="locale",
                                 languages=[locale])

        tr.gettext = i18nfix.wrap_gettext(tr.gettext)

        env.install_gettext_translations(tr, newstyle=True)

        content = tmpl.render(lang=locale,
                              lang_flag=lang_flags[locale],
                              lang_flags=lang_flags,
                              lang_full=langs_full[locale],
                              langs_full=langs_full,
                              url=url,
                              self_localized=self_localized,
                              url_localized=url_localized,
                              svg_localized=svg_localized,
                              filename=name + "." + ext)
        out_name = "./rendered/" + locale + "/" + in_file.replace('template/', '').rstrip(".j2")
        os.makedirs("./rendered/" + locale, exist_ok=True)
        with codecs.open(out_name, "w", encoding='utf-8') as f:
            f.write(content)
