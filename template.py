#!/usr/bin/env python3
# coding: utf-8
#
# Copyright (C) 2019 Alexandros Theodotou <alex at zrythm dot org>
# Copyright (C) 2017, 2018, 2019 GNUnet e.V.
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.
#
# ----
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
import polib

# for news
import pprint
import feedparser
import datetime
from dateutil.parser import parse

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
        "pt_BR": "Português BR",
        "cs": "Czech",
        "de": "Deutsch",
        "pl": "Polski",
        "da": "Dansk",
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
        "pt_BR": "[pt]",
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
git_base_url = 'https://git.zrythm.org/cgit/'
git_url = git_base_url + 'zrythm'
git_web_url = git_base_url + 'zrythm-web'
issue_tracker = 'https://redmine.zrythm.org/projects/zrythm/issues'
git_blob_url = git_url + '/tree'
pronunciation = 'ziˈrɪðəm'
releases_url = 'https://www.zrythm.org/releases/'
aur_git_url = 'https://aur.archlinux.org/packages/zrythm-git/'
aur_stable_url = 'https://aur.archlinux.org/packages/zrythm/'
obs_package_url = 'https://software.opensuse.org//download.html?project=home%3Aalextee&package=zrythm'
copr_package_url = 'https://copr.fedorainfracloud.org/coprs/ycollet/linuxmao/package/zrythm/'
freshports_url = 'https://www.freshports.org/audio/zrythm/'

# get latest version
from subprocess import check_output
version = check_output('git ls-remote --tags https://git.zrythm.org/git/zrythm | grep -o "refs/tags/v[0-9]*\.[0-9]*\.[0-9]*" | sort -r | head -n 1 | grep -o "[^\/]*$"', shell=True).decode("utf-8")[1:]

# for news
feed = feedparser.parse('https://savannah.nongnu.org/news/atom.php?group=zrythm')
pp = pprint.PrettyPrinter(indent=2)
news = feed['entries'][0:4]

for in_file in glob.glob("template/*.j2"):
    name, ext = re.match(r"(.*)\.([^.]+)$", in_file.rstrip(".j2")).groups()
    tmpl = env.get_template(in_file)

    def self_localized(other_locale):
        """
        Return URL for the current page in another locale.
        """
        return "https://www.zrythm.org/" + other_locale + "/" + in_file.replace('template/', '').rstrip(".j2")

    def url_localized(filename):
        return "../" + locale + "/" + filename

    def svg_localized(filename):
        lf = filename + "." + locale + ".svg"
        if locale == "en" or not os.path.isfile(lf):
            return "../" + filename + ".svg"
        else:
            return "../" + lf

    # truncate html for news
    # taken from https://djangosnippets.org/snippets/1477/ under the
    # terms of service states that "you grant any third party who sees the code
    # you post a royalty-free, non-exclusive license to copy and distribute
    # that code and to make and distribute derivative works based on that code"
    import re
    tag_end_re = re.compile(r'(\w+)[^>]*>')
    entity_end_re = re.compile(r'(\w+;)')
    def truncatehtml(string, length, ellipsis='...'):
        """Truncate HTML string, preserving tag structure and character entities."""
        length = int(length)
        output_length = 0
        i = 0
        pending_close_tags = {}

        while output_length < length and i < len(string):
            c = string[i]

            if c == '<':
                # probably some kind of tag
                if i in pending_close_tags:
                    # just pop and skip if it's closing tag we already knew about
                    i += len(pending_close_tags.pop(i))
                else:
                    # else maybe add tag
                    i += 1
                    match = tag_end_re.match(string[i:])
                    if match:
                        tag = match.groups()[0]
                        i += match.end()

                        # save the end tag for possible later use if there is one
                        match = re.search(r'(</' + tag + '[^>]*>)', string[i:], re.IGNORECASE)
                        if match:
                            pending_close_tags[i + match.start()] = match.groups()[0]
                    else:
                        output_length += 1 # some kind of garbage, but count it in

            elif c == '&':
                # possible character entity, we need to skip it
                i += 1
                match = entity_end_re.match(string[i:])
                if match:
                    i += match.end()

                # this is either a weird character or just '&', both count as 1
                output_length += 1
            else:
                # plain old characters

                skip_to = string.find('<', i, i + length)
                if skip_to == -1:
                    skip_to = string.find('&', i, i + length)
                if skip_to == -1:
                    skip_to = i + length

                # clamp
                delta = min(skip_to - i,
                            length - output_length,
                            len(string) - i)

                output_length += delta
                i += delta

        output = [string[:i]]
        if output_length == length:
            output.append(ellipsis)

        for k in sorted(pending_close_tags.keys()):
            output.append(pending_close_tags[k])

        return "".join(output)

    def url(x):
        # TODO: look at the app root environment variable
        # TODO: check if file exists
        return "../" + x

    # remove fuzzies
    for dirname, dirnames, filenames in os.walk('locale'):
        for filename in filenames:
            try: ext = filename.rsplit('.', 1)[1]
            except: ext = ''
            if ext == 'po':
                po = polib.pofile(os.path.join(dirname, filename))
                for entry in po.fuzzy_entries():
                    entry.msgstr = ''
                    if entry.msgid_plural: entry.msgstr_plural['0'] = ''
                    if entry.msgid_plural and '1' in entry.msgstr_plural: entry.msgstr_plural['1'] = ''
                    if entry.msgid_plural and '2' in entry.msgstr_plural: entry.msgstr_plural['2'] = ''
                    entry.flags.remove('fuzzy')
                po.save()

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
                              git_base_url=git_base_url,
                              git_url=git_url,
                              git_web_url=git_web_url,
                              aur_git_url=aur_git_url,
                              aur_stable_url=aur_stable_url,
                              freshports_url=freshports_url,
                              obs_package_url=obs_package_url,
                              copr_package_url=copr_package_url,
                              releases_url=releases_url,
                              news=news,
                              datetime_parse=parse,
                              issue_tracker=issue_tracker,
                              git_blob_url=git_blob_url,
                              version=version,
                              pronunciation=pronunciation,
                              self_localized=self_localized,
                              url_localized=url_localized,
                              svg_localized=svg_localized,
                              truncatehtml=truncatehtml,
                              filename=name + "." + ext)
        out_name = "./rendered/" + locale + "/" + in_file.replace('template/', '').rstrip(".j2")
        os.makedirs("./rendered/" + locale, exist_ok=True)
        with codecs.open(out_name, "w", encoding='utf-8') as f:
            f.write(content)
