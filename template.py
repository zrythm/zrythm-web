#!/usr/bin/env python3
# coding: utf-8
#
# Copyright (C) 2019-2020 Alexandros Theodotou <alex at zrythm dot org>
#
# This file is part of Zrythm
#
# Zrythm is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Zrythm is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# This file incorporates work covered by the following copyright and
# permission notice:
#
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
import requests

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
        "ar": "العربية",
        "cs": "Czech",
        "da": "Dansk",
        "de": "Deutsch",
        "en": "English",
        "en_GB": "English UK",
        "el": "Ελληνικά",
        "es": "Español",
        "et": "Eeti",
        "fi": "Suomi",
        "fr": "Français",
        "gd": "Gaelic",
        "gl": "Galego",
        "hi": "हिन्दी",
        "it": "Italiano",
        "ja": "日本語",
        "ko": "한국어",
        "nb_NO": "Bokmål",
        "nl": "Nederlands",
        "pl": "Polski",
        "pt": "Português",
        "pt_BR": "Português BR",
        "ru": "русский",
        "sv": "Svenska",
        "zh": "中文",
        }
lang_flags = {
        "ar": "[ar]",
        "cs": "[cs]",
        "da": "[da]",
        "de": "[de]",
        "en": "[en]",
        "en_GB": "[en]",
        "el": "[el]",
        "es": "[es]",
        "et": "[et]",
        "fi": "[fi]",
        "fr": "[fr]",
        "gd": "[gd]",
        "gl": "[gl]",
        "hi": "[hi]",
        "it": "[it]",
        "ja": "[ja]",
        "ko": "[ko]",
        "nb_NO": "[nb]",
        "nl": "[nl]",
        "pl": "[pl]",
        "pt": "[pt]",
        "pt_BR": "[pt]",
        "ru": "[ru]",
        "sv": "[sv]",
        "zh": "[zh]",
        }
git_base_url = 'https://git.zrythm.org/cgit/'
git_url = git_base_url + 'zrythm'
git_web_url = git_base_url + 'zrythm-web'
issue_tracker = 'https://redmine.zrythm.org/projects/zrythm/issues'
git_blob_url = git_url + '/tree'
pronunciation = 'ziˈrɪðəm'
releases_url = 'https://www.zrythm.org/releases/'
downloads_url = 'https://www.zrythm.org/downloads/'
aur_git_url = 'https://aur.archlinux.org/packages/zrythm-git/'
aur_stable_url = 'https://aur.archlinux.org/packages/zrythm/'
obs_package_url = 'https://software.opensuse.org//download.html?project=home%3Aalextee&package=zrythm'
copr_package_url = 'https://copr.fedorainfracloud.org/coprs/ycollet/linuxmao/package/zrythm/'
freshports_url = 'https://www.freshports.org/audio/zrythm/'

usd_to_gbp = 0.77

# get monthly orders
orders_url = 'https://{}:{}@www.sendowl.com/api/v1/orders'.format(
        os.getenv('SENDOWL_KEY'), os.getenv('SENDOWL_SECRET'))
headers = {
    'Accept': 'application/json',
    'Content-type': 'application/json',
    'Accept-Charset': 'UTF-8',
    }
payload = {
    'from': datetime.datetime.utcnow().replace(day=1).strftime('%Y-%m-%d'),
    'to': datetime.datetime.utcnow().strftime('%Y-%m-%d'),
    'state': 'complete',
    }
r = requests.get(orders_url, params=payload, headers=headers)
if r.status_code == 200:
    monthly_earning = 0
    num_monthly_orders = 0
    for _order in r.json():
        num_monthly_orders += 1
        order = _order['order']
        profit = float(order['settled_gross']) - float(order['settled_gateway_fee'])
        if order['settled_currency'] == 'USD':
            profit *= usd_to_gbp
        print ('adding {} sendowl earnings'.format(profit))
        monthly_earning += profit
else:
    print (r.json())

# get paypal earnings
access_token_url = 'https://{}:{}@api.paypal.com/v1/oauth2/token'.format(
        os.getenv('PAYPAL_CLIENT_ID'), os.getenv('PAYPAL_SECRET'))
headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en_US',
    }
payload = {
    'grant_type': 'client_credentials',
    }
r = requests.post(access_token_url, params=payload, headers=headers)
if r.status_code == 200:
    access_token = r.json()['access_token']
    transactions_url = 'https://api.paypal.com/v1/reporting/transactions'
    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json',
        'Accept-Charset': 'UTF-8',
        'Authorization': 'Bearer ' + access_token,
        }
    payload = {
        'start_date': datetime.datetime.utcnow().replace(day=1,tzinfo=datetime.timezone.utc).astimezone().replace(microsecond=0).isoformat(),
        'end_date': datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).astimezone().replace(microsecond=0).isoformat(),
        'transaction_status': 'S',
        }
    r = requests.get(transactions_url, params=payload, headers=headers)
    if r.status_code == 200:
        for _tx in r.json()['transaction_details']:
            tx = _tx['transaction_info']
            if 'transaction_subject' in tx and tx['transaction_subject'] == 'Zrythm subscription':
                profit = float(tx['transaction_amount']['value']) + float(tx['fee_amount']['value'])
                if tx['transaction_amount']['currency_code'] == 'USD':
                    profit *= usd_to_gbp
                if profit > 0:
                    print ('adding {} paypal earnings'.format(profit))
                    monthly_earning += profit
    else:
        print (r.json())
else:
    print (r.json())

# get liberapay earnings
r = requests.get("https://liberapay.com/Zrythm/public.json")
if r.status_code == 200:
    profit = float(r.json()['receiving']['amount']) * 4.0
    profit = float('%.2f' % profit)
    print ('adding {} liberapay earnings'.format(profit))
    monthly_earning += profit
else:
    print (r.json())

monthly_earning_str = '{0:.2f}'.format(monthly_earning)

# get latest version
from subprocess import check_output
version = check_output('git ls-remote --tags https://git.zrythm.org/git/zrythm | grep -o "refs/tags/v[0-9]*\.[0-9]*\.[0-9]*" | sort -r | head -n 1 | grep -o "[^\/]*$"', shell=True).decode("utf-8")[1:]

# for news
feed = feedparser.parse('https://savannah.nongnu.org/news/atom.php?group=zrythm')
pp = pprint.PrettyPrinter(indent=2)
news = feed['entries'][0:4]

class Plugin:
    def __init__(self,name,is_img_static,img,summary,features):
        self.name = name
        self.is_img_static = is_img_static
        self.img = img
        self.summary = summary
        self.features = features

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

    for l in langs_full.keys():
        locale = l

        tr = gettext.translation("messages",
                                 localedir="locale",
                                 languages=[locale],
                                 # only fallback to no translations for en
                                 fallback= locale == 'en')

        tr.gettext = i18nfix.wrap_gettext(tr.gettext)
        _ = tr.gettext

        env.install_gettext_translations(tr, newstyle=True)

        # plugins
        plugins = [
            Plugin(
                'ZChordz', True, 'zchordz-mar-21-2020.png',
                _('ZChordz maps the chords of a minor or major scale to white keys'),
                [ _('Major or minor scale'),
                    _('Velocity multiplier per note') ]),
            Plugin(
                'ZLFO', False,
                'https://git.zrythm.org/cgit/ZLFO/plain/screenshots/2020_feb_12_zlfo.png',
                _('ZLFO is a fully featured LFO for CV-based automation'),
                [ _('Multi-oscillator with custom wave'),
                    _('Phase shift'),
                    _('Vertical/horizontal inversion'),
                    _('Step mode'),
                    _('Editable range'),
                    _('Sync to host or free-form') ]),
            Plugin(
                'ZSaw', True, 'zsaw-mar-21-2020.png',
                _('ZSaw is a supersaw synth with 1 parameter'),
                [ _('7 sawtooth oscillators'),
                    _('Single knob to control detune') ]),
            ]

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
                              downloads_url=downloads_url,
                              news=news,
                              datetime_parse=parse,
                              num_monthly_orders=num_monthly_orders,
                              monthly_earning=monthly_earning,
                              monthly_earning_str=monthly_earning_str,
                              issue_tracker=issue_tracker,
                              plugins=plugins,
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
