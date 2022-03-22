#!/usr/bin/env python3
# coding: utf-8
#
# Copyright (C) 2019-2022 Alexandros Theodotou <alex at zrythm dot org>
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
import urllib3
import polib
import requests
import semver

# for news
import datetime
import dateutil
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

PAYPAL_CLIENT_ID = os.getenv ('PAYPAL_CLIENT_ID')
PAYPAL_SECRET = os.getenv ('PAYPAL_SECRET')
ZRYTHM_ACCOUNTS_TOKEN = os.getenv ('ZRYTHM_ACCOUNTS_TOKEN')

fetch_orders = PAYPAL_CLIENT_ID and PAYPAL_SECRET and ZRYTHM_ACCOUNTS_TOKEN
verify_trial_package_urls = os.getenv ('VERIFY_TRIAL_PACKAGE_URLS') == 'YES'
get_version = os.getenv ('GET_VERSION') == 'YES'

# Note: also edit the Makefile when adding languages
langs_full = {
    'af_ZA': ['🇿🇦', 'Afrikaans', 'USD'],
    'ar': ['🇦🇪', 'العربية', 'USD'],
    'ca': ['🇦🇩', 'Català', 'EUR'],
    'cs': ['🇨🇿', 'Czech', 'EUR'],
    'da': ['🇩🇰', 'Dansk', 'EUR'],
    'de': ['🇩🇪', 'Deutsch', 'EUR'],
    'en': ['🇺🇸', 'English US', 'USD'],
    'en_GB': ['🇬🇧', 'English UK', 'GBP'],
    'el': ['🇬🇷', 'Ελληνικά', 'EUR'],
    'es': ['🇪🇸', 'Español', 'EUR'],
    'et': ['🇪🇪', 'Eeti', 'EUR'],
    'fi': ['🇫🇮', 'Suomi', 'EUR'],
    'fr': ['🇫🇷', 'Français', 'EUR'],
    'gd': ['🏴󠁧󠁢󠁳󠁣󠁴󠁿', 'Gaelic', 'GBP'],
    'gl': ['🇪🇸', 'Galego', 'EUR'],
    'he': ['🇮🇱', 'עִבְרִית', 'USD'],
    'hi': ['🇮🇳', 'हिन्दी', 'USD'],
    'id': ['🇮🇩', 'bahasa Indonesia', 'USD'],
    'it': ['🇮🇹', 'Italiano', 'EUR'],
    'ja': ['🇯🇵', '日本語', 'JPY'],
    'ko': ['🇰🇷', '한국어', 'USD'],
    'nb_NO': ['🇳🇴', 'Bokmål', 'EUR'],
    'nl': ['🇳🇱', 'Nederlands', 'EUR'],
    'pl': ['🇵🇱', 'Polski', 'EUR'],
    'pt': ['🇵🇹', 'Português', 'EUR'],
    'pt_BR': ['🇧🇷', 'Português BR', 'USD'],
    'ru': ['🇷🇺', 'Русский', 'RUB'],
    'sl': ['🇸🇮', 'Slovenščina', 'EUR'],
    'sv': ['🇸🇪', 'Svenska', 'EUR'],
    'th': ['🇹🇭', 'ภาษาไทย', 'USD'],
    'tr': ['🇹🇷', 'Türkiye', 'USD'],
    'uk': ['🇺🇦', 'Українська', 'EUR'],
    'vi': ['🇻🇳', 'Tiếng Việt', 'USD'],
    'zh_CN': ['🇨🇳', '简体中文', 'CNY'],
    'zh_TW': ['🇹🇼', '繁體中文', 'TWD'],
    }
git_url = 'https://git.sr.ht/~alextee/zrythm'
feature_tracker = 'https://todo.sr.ht/~alextee/zrythm-feature'
bug_tracker = 'https://todo.sr.ht/~alextee/zrythm-bug'
pronunciation = 'ziˈrɪðəm'
releases_url = 'https://www.zrythm.org/releases/'
downloads_url = 'https://www.zrythm.org/downloads/'
s3_bucket_url = 'https://sendowl-bucket.s3.amazonaws.com'
aur_git_url = 'https://aur.archlinux.org/packages/zrythm-git/'
aur_stable_url = 'https://aur.archlinux.org/packages/zrythm/'
obs_package_url = 'https://software.opensuse.org//download.html?project=home%3Aalextee&package=zrythm'
copr_package_url = 'https://copr.fedorainfracloud.org/coprs/ycollet/linuxmao/package/zrythm/'
freshports_url = 'https://www.freshports.org/audio/zrythm/'

currency_symbols = {
    'USD': '$',
    'GBP': '£',
    'EUR': '€',
    'JPY': '¥',
    'CNY': '¥',
    'TWD': 'NT$',
    'RUB': '₽',
    }
forex_url = 'https://open.er-api.com/v6/latest/GBP'
headers = {
    'Accept': 'application/json',
    'Content-type': 'application/json',
    'Accept-Charset': 'UTF-8',
    }
print ('getting forex rates...')
currency_rates = { }
r = requests.get(forex_url, headers=headers)
if r.status_code == 200:
    res_json = r.json ()
    rates = res_json['rates']
    for sym in currency_symbols.keys():
        currency_rates[sym] = float (rates[sym])
else:
    print (r.json())
    exit (1)

prev_month_earning = 100
monthly_earning = 0
num_monthly_orders = 0

# get monthly orders
if fetch_orders:
    orders_url = 'https://accounts.zrythm.org/api/v1/orders/'
    headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json',
        'Accept-Charset': 'UTF-8',
        'Authorization': 'Token %s' % os.getenv ('ZRYTHM_ACCOUNTS_TOKEN'),
        }
    payload = {
        'limit': '100',
        'status': 'Completed',
        'ordering': '-created_at',
        }
    print ('getting zrythm-accounts orders...')
    r = requests.get(orders_url, params=payload, headers=headers)
    if r.status_code == 200:
        start_datetime = datetime.datetime.utcnow().replace(day=1,tzinfo=datetime.timezone.utc).astimezone().replace(microsecond=0)
        # TODO change to following next month
        # start_datetime = datetime.datetime.utcnow().replace(day=1,tzinfo=datetime.timezone.utc).astimezone().replace(microsecond=0)
        for order in r.json()['results']:
            product = order['product']
            if product['type'] == 'Subscription':
                continue
            created_at = dateutil.parser.isoparse (order['created_at'])
            if created_at < start_datetime:
                continue
            amount = float (product['price_gbp'])
            amount -= (amount * 0.05)
            print ('adding {} zrythm accounts earnings'.format(amount))
            monthly_earning += amount
            num_monthly_orders += 1
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
                    amount = float(tx['transaction_amount']['value'])
                    if 'fee_amound' in tx:
                        amount += float(tx['fee_amount']['value'])
                    if tx['transaction_amount']['currency_code'] == 'USD':
                        amount *= usd_to_gbp
                    if amount > 0:
                        print ('adding {} paypal subscription earnings'.format(amount))
                        monthly_earning += amount
                elif 'invoice_id' not in tx and tx['transaction_event_code'] == 'T0000':
                    amount = float(tx['transaction_amount']['value'])
                    if 'fee_amound' in tx:
                        amount += float(tx['fee_amount']['value'])
                    if tx['transaction_amount']['currency_code'] == 'USD':
                        amount *= usd_to_gbp
                    elif tx['transaction_amount']['currency_code'] == 'EUR':
                        amount *= eur_to_gbp
                    if amount > 0:
                        print ('adding {} paypal custom donation earnings'.format(amount))
                        monthly_earning += amount
        else:
            print (r.json())
    else:
        print (r.json())

# get liberapay earnings
    for lp_account in [ 'Zrythm', 'alextee' ]:
        r = requests.get('https://liberapay.com/' + lp_account + '/public.json')
        if r.status_code == 200:
            amount = float(r.json()['receiving']['amount']) * 4.0
            amount = float('%.2f' % amount)
            print ('adding {} liberapay earnings'.format(amount))
            monthly_earning += amount
        else:
            if r:
                print (r.json())
            else:
                print ('No response from liberapay')

# add opencollective earnings
    r = requests.get("https://opencollective.com/zrythm.json")
    if r.status_code == 200:
        amount = float(r.json()['yearlyIncome']) / 1200.0
        amount = amount / currency_rates['USD']
        amount = float('%.2f' % amount)
        print ('adding {} opencollective earnings (estimated)'.format(amount))
        monthly_earning += amount
    else:
            if r:
                print (r.json())
            else:
                print ('No response from OpenCollective')

monthly_earning_str = '{0:.2f}'.format(monthly_earning)
prev_month_earning_str = '{0:.2f}'.format(prev_month_earning)
prev_month_comparison_perc = '{0:.0f}'.format(100 * (monthly_earning / prev_month_earning))

if get_version:
# get latest version
    from subprocess import check_output
    versions = check_output('git ls-remote --tags https://git.zrythm.org/zrythm/zrythm | grep -o "refs/tags/v[0-9]*\.[0-9]*\.[0-9]*-beta\.[0-9]*\.[0-9]*\.[0-9]*$" | sed -e "s/v//" | sort -r | grep -o "[^\/]*$"', shell=True).decode("utf-8").strip ()
    latest_ver = "0.0.0"
    for ver in versions.split('\n'):
        if (semver.compare(ver, latest_ver) > 0):
            latest_ver = ver
    print ('normal version: ' + latest_ver)
    version = latest_ver.replace ('-', '.')
    print ('version: ' + version)
else:
    version = '1'

def check_url(url):
    print ('checking ' + url + '...')
    try:
        with requests.get(url, stream=True) as response:
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError:
                print ('error fetching ' + url + ': ' + str (status))
                exit (1)
    except requests.exceptions.ConnectionError:
        print ('error fetching ' + url + ': ' + str (status))
        exit (1)

# verify that tarball and trials exist
if verify_trial_package_urls:
    print ('verifying release and trial packages...')
    check_url (releases_url + 'zrythm-' + latest_ver + '.tar.xz')
    check_url (downloads_url + 'zrythm-trial-' + version + '-x86_64.AppImage')
    check_url (downloads_url + 'zrythm-trial-' + version + '-x86_64.flatpak')
    check_url (downloads_url + 'zrythm-trial-' + version + '-installer.zip')
    check_url (downloads_url + 'zrythm-trial-' + version + '-ms-setup.exe')
    check_url (downloads_url + 'zrythm-trial-' + version + '-osx-installer.zip')
    print ('done')

def url(x):
    # TODO: look at the app root environment variable
    # TODO: check if file exists
    return "../" + x

screenshot = url('static/images/screenshots/mar-16-2022.png')

class Plugin:
    def __init__(self,name,is_img_static,img,summary,features):
        self.name = name
        self.is_img_static = is_img_static
        self.img = img
        self.summary = summary
        self.features = features

class FeatureGroup:
    def __init__(self,title,features):
        self.title = title
        self.features = features

class Feature:
    def __init__(self,title,img,summary):
        self.title = title
        self.img = img
        self.summary = summary

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
        locale_for_accounts = l.lower().replace ('_', '-').replace ('zh-cn', 'zh-hans').replace ('zh-tw', 'zh-hant')

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
                'https://git.zrythm.org/alex/ZLFO/raw/branch/master/screenshots/2020_feb_12_zlfo.png',
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

        # features
        feature_groups = [
            FeatureGroup(
                _('Intuitive Editing'),
                [
                    Feature(
                        _('Flexible Select Tool'), 'piano-roll.gif',
                        _('Select, move, resize, clone, link, loop, delete and cut objects with a single tool.')),
                    Feature(
                        _('Extensive Toolbox'), 'https://manual.zrythm.org/en/_images/toolbox.png',
                        _('Extend select tool functionality by switching to the Edit, Cut, Erase, Ramp or Audition tools.')),
                    Feature(
                        _('Adaptive Snapping'), 'https://manual.zrythm.org/en/_images/snap-grid-options.png',
                        _('Snapping behavior adjusts to the current zoom level.')),
                    Feature(
                        _('Looping'), 'https://manual.zrythm.org/en/_images/looping-regions.png',
                        _('Loop audio, MIDI, automation and chord clips.')),
                ]),
            FeatureGroup(
                _('Featureful Timeline'),
                [
                    Feature(
                        _('Track Lanes'), 'https://manual.zrythm.org/en/_images/track-lanes.png',
                        _('Add multiple layers of audio/MIDI to the same track using track lanes.')),
                    Feature(
                        _('Bounce in Place'), 'bounce-in-place.gif',
                        _('Quickly bounce selected material to audio.')),
                    Feature(
                        _('Stretching'), 'piano-roll.gif',
                        _('Stretch any type of region')),
                ]),
            FeatureGroup(
                _('Powerful Editors'),
                [
                    Feature(
                        _('Piano Roll'), 'chord-highlighting.png',
                        _('Create, edit and arrange MIDI events in a dedicated piano roll with chord integration.')),
                    Feature(
                        _('Drum View'), 'https://manual.zrythm.org/en/_images/drum-mode.png',
                        _('One-click switch to drum view for editing single-hit instruments.')),
                    Feature(
                        _('Velocity Editor'), 'https://manual.zrythm.org/en/_images/ramp-tool.png',
                        _('Edit multiple velocities simultaneously with the select tool or draw with the pencil or ramp tool.')),
                    Feature(
                        _('Audio Editor'), 'https://manual.zrythm.org/en/_images/audio-editor.png',
                        _('Adjust fades/gain and edit parts of audio clips using audio functions inside the audio editor.')),
                    Feature(
                        _('List Editors'), 'https://manual.zrythm.org/en/_images/timeline-event-viewer.png',
                        _('Edit object parameters manually in the event viewer.')),
                    Feature(
                        _('Editor Functions'), 'piano-roll.gif',
                        _('Quickly apply functions like Legato, Invert and Fade Out to the selected objects.')),
                    Feature(
                        _('External App Integration'), 'https://manual.zrythm.org/en/_images/edit-audio-external-app.png',
                        _('Edit selected audio parts in any external app.')),
                ]),
            FeatureGroup(
                _('Recording Capabilities'),
                [
                    Feature(
                        _('Audio/MIDI Recording'), 'https://manual.zrythm.org/en/_images/audio-track-recording.png',
                        _('Record audio/MIDI from any of your devices, or even from other apps using JACK.')),
                    Feature(
                        _('Comprehensive Recording Settings'), 'https://manual.zrythm.org/en/_images/recording-modes.png',
                        _('Use punch in/punch out, record on MIDI input, and optionally create multiple takes.')),
                    Feature(
                        _('Automation Recording'), 'https://manual.zrythm.org/en/_images/automation-touch.png',
                        _('Record automation in latch/touch mode.')),
                    Feature(
                        _('Device Controls'), 'https://manual.zrythm.org/en/_images/midi-bindings.png',
                        _('Bind your device knobs to controls inside Zrythm and record your actions.')),
                ]),
            FeatureGroup(
                _('Mixing Capabilities'),
                [
                    Feature(
                        _('Group Tracks'), 'https://manual.zrythm.org/en/_images/audio-group-track.png',
                        _('Organize audio/MIDI signal groups with group tracks.')),
                    Feature(
                        _('Aux Sends'), 'https://manual.zrythm.org/en/_images/track-sends.png',
                        _('Easily route signals to FX tracks and plugin sidechain inputs.')),
                    Feature(
                        _('In-Context Listening'), 'https://manual.zrythm.org/en/_images/channel.png',
                        _('Listen to specified tracks in the context of the mix by dimming down every other track.')),
                    Feature(
                        _('Monitor Section'), 'https://manual.zrythm.org/en/_images/monitor-out-knob.png',
                        _('Change listen/mute/solo behavior and adjust what goes to your speakers.')),
                ]),
            FeatureGroup(
                _('Unlimited Automation'),
                [
                    Feature(
                        _('Anywhere-to-Anywhere Connections'), 'anywhere-to-anywhere-connections.gif',
                        _('Connect anything to anything.')),
                    Feature(
                        _('Automation Curves'), 'automation-curves.gif',
                        _('Automate parameters with straight lines or curves, choosing from multiple curve algorithms, such as Exponential and Elliptic curves.')),
                    Feature(
                        _('Envelopes'), 'https://manual.zrythm.org/en/_images/modulators-tab.png',
                        _('Automate parameters with CV signals or envelopes, including macro knobs and LFO plugins such as ZLFO.')),
                    Feature(
                        _('Automate Anything'), 'https://manual.zrythm.org/en/_images/tempo-track.png',
                        _('Automate any possible parameter, including the project\'s BPM and time signature.')),
                ]),
            FeatureGroup(
                _('Intuitive User Interface'),
                [
                    Feature(
                        _('Detachable Views'), 'https://manual.zrythm.org/en/_images/timeline-detached.png',
                        _('Detach views from any panel and work efficiently with multi-monitor setups.')),
                    Feature(
                        _('Searchable Preferences'), 'https://manual.zrythm.org/en/_images/preferences-searching.png',
                        _('Start typing to locate the preference you\'re looking for.')),
                    Feature(
                        _('Inspector Pages'), 'https://manual.zrythm.org/en/_images/track-inspector.png',
                        _('Edit all track and plugin parameters in the inspector.')),
                ]),
            FeatureGroup(
                _('Plugin Capabilities'),
                [
                    Feature(
                        _('Plugin Support'), 'plugin-showcase.png',
                        _('Thanks to Carla, Zrythm supports a variety of plugin formats including LV2, VST2, VST3 and AU.')),
                    Feature(
                        _('SoundFonts as Plugins'), 'piano-roll.gif',
                        _('Use SFZ and SF2 soundfonts as instrument plugins.')),
                    Feature(
                        _('Flexible Plugin Browser'), 'https://manual.zrythm.org/en/_images/plugin-browser.png',
                        _('Easily filter plugins by author, format or category, and organize your favorite plugins with plugin collections.')),
                    Feature(
                        _('Plugin Bridging'), 'https://manual.zrythm.org/en/_images/open-plugin-bridged.png',
                        _('Sandbox plugins by opening them in bridge mode.')),
                    Feature(
                        _('Automatable Bypass Mode'), 'piano-roll.gif',
                        _('Easily bypass plugins in the signal chain with an automatable control.')),
                ]),
            FeatureGroup(
                _('Comprehensive Import/Export'),
                [
                    Feature(
                        _('File Browser'), 'https://manual.zrythm.org/en/_images/file-browser.png',
                        _('Browse and audition MIDI and audio files, and organize your favorite paths with favorites.')),
                    Feature(
                        _('Audio Files'), 'https://manual.zrythm.org/en/_images/file-filter-buttons.png',
                        _('Import or export any format supported by libsndfile, with additional MP3 import support.')),
                    Feature(
                        _('MIDI'), 'piano-roll.gif',
                        _('Import or export any part of the project in MIDI Type 0 or Type 1 formats.')),
                    Feature(
                        _('Stem Export'), 'https://manual.zrythm.org/en/_images/export-dialog.png',
                        _('Export stems for specific tracks and share them with other producers.')),
                ]),
            FeatureGroup(
                _('Chord Assistance'),
                [
                    Feature(
                        _('Chord Audition'), 'https://manual.zrythm.org/en/_images/chord-pad.png',
                        _('Quickly listen to chords by clicking the pads or pressing notes on your MIDI keyboard, and drag-and-drop chords to the timeline.')),
                    Feature(
                        _('Chord Editing'), 'https://manual.zrythm.org/en/_images/chord-selector.png',
                        _('Invert chords with a single click or use the chord selector to choose any chord, with an option to filter chords in the current scale.')),
                    Feature(
                        _('Recordable Chord Track'), 'https://manual.zrythm.org/en/_images/chord-track.png',
                        _('Dictate or record the scale and chord progression of the project, and optionally route the output to an instrument.')),
                    Feature(
                        _('Chord Presets'), 'piano-roll.gif',
                        _('Generate chords from a wide range of scales, load included chord presets for various genres, or save your own.')),
                ]),
            FeatureGroup(
                _('Never Lose Work'),
                [
                    Feature(
                        _('Project Backups'), 'piano-roll.gif',
                        _('Backups taken automatically at user-specified intervals.')),
                    Feature(
                        _('Undoable Actions'), 'https://manual.zrythm.org/en/_images/undo-multiple.png',
                        _('Almost every user action is undoable.')),
                    Feature(
                        _('Serializable Undo History'), 'piano-roll.gif',
                        _('Keep your undo history when saving projects.')),
                ]),
            FeatureGroup(
                _('Scripting'),
                [
                    Feature(
                        _('Extend Zrythm'), 'piano-roll.gif',
                        _('Extend the capabilities of Zrythm by editing its state using GNU Guile scripts.')),
                    Feature(
                        _('Custom Editor Functions'), 'piano-roll.gif',
                        _('Implement your own MIDI/audio/automation functions (coming soon).')),
                    Feature(
                        _('Project Generation'), 'piano-roll.gif',
                        _('Generate projects with GNU Guile scripts.')),
                ]),
            FeatureGroup(
                _('Optimized Performance'),
                [
                    Feature(
                        _('Hardware accelerated UI'), 'https://manual.zrythm.org/en/_images/first-run-interface.png',
                        _('Most of the user interface is drawn on the GPU thanks to GTK4.')),
                    Feature(
                        _('SIMD-optimized DSP'), 'piano-roll.gif',
                        _('Zrythm uses lsp-dsp-lib which implements SIMD extensions such as SSE, AVX and FMA when available to speed up audio processing and minimize DSP usage.')),
                    Feature(
                        _('Extensive Caching'), 'piano-roll.gif',
                        _('Expensive computations are pre-calculated and the result is re-used during processing.')),
                ]),
            FeatureGroup(
                _('Cross-Platform Support'),
                [
                    Feature(
                        _('Multiple Platforms'), 'piano-roll.gif',
                        _('Zrythm is designed to run on a wide variety of platforms and architectures including x86 architectures, PowerPC, RISC-V, ARMv7 and ARMv8.')),
                    Feature(
                        _('Multiple Backends'), 'audio-backend-selection.png',
                        _('Support for almost all major audio and MIDI backends, including JACK/PipeWire, Windows MME, WASAPI and Core Audio/MIDI.')),
                ]),
            FeatureGroup(
                _('Localization'),
                [
                    Feature(
                        _('Localized UI'), 'screenshots/feb-15-2021.png',
                        _('Use Zrythm in your preferred language.')),
                    Feature(
                        _('Easily Add Translations'), 'piano-roll.gif',
                        _('Add missing translations and locales on Weblate.')),
                ]),
            FeatureGroup(
                _('User Liberty'),
                [
                    Feature(
                        _('Free Software'), 'programming.png',
                        _('With all source code released as copyleft free software, Zrythm is committed to ensuring the freedom of computer users.')),
                    Feature(
                        _('Open Standards'), 'piano-roll.gif',
                        _('Zrythm supports open standards such as MIDI, LV2, FLAC and OGG.')),
                    Feature(
                        _('Cooperation'), 'piano-roll.gif',
                        _('We work with the free software community to ensure Zrythm works without issues on all libre platforms.')),
                ]),
            ]

        currency_for_locale = langs_full[locale][2]
        currency_sym_for_locale = currency_symbols[currency_for_locale]
        single_price_for_locale = round (10 * currency_rates[currency_for_locale])
        bundle_price_for_locale = round (25 * currency_rates[currency_for_locale])
        subscription_price_for_locale = round (35 * currency_rates[currency_for_locale])
        monthly_earning_for_locale = round (monthly_earning * currency_rates[currency_for_locale])
        # if JPY, round again to 100s
        if currency_for_locale == 'JPY' or currency_for_locale == 'RUB':
            single_price_for_locale = round (single_price_for_locale, -2)
            bundle_price_for_locale = round (bundle_price_for_locale, -2)
            subscription_price_for_locale = round (subscription_price_for_locale, -2)
            monthly_earning_for_locale = round (monthly_earning_for_locale, -2)
        single_price_for_locale = '{}{}'.format (currency_sym_for_locale, single_price_for_locale)
        bundle_price_for_locale = '{}{}'.format (currency_sym_for_locale, bundle_price_for_locale)
        subscription_price_for_locale = '{}{}'.format (currency_sym_for_locale, subscription_price_for_locale)
        monthly_earning_str = '{}{}'.format (currency_sym_for_locale, monthly_earning_for_locale)

        content = tmpl.render(lang=locale,
                              lang_for_accounts=locale_for_accounts,
                              lang_full=langs_full[locale],
                              langs_full=langs_full,
                              currency_for_locale=currency_for_locale,
                              single_price_for_locale=single_price_for_locale,
                              bundle_price_for_locale=bundle_price_for_locale,
                              subscription_price_for_locale=subscription_price_for_locale,
                              url=url,
                              git_url=git_url,
                              aur_git_url=aur_git_url,
                              aur_stable_url=aur_stable_url,
                              freshports_url=freshports_url,
                              obs_package_url=obs_package_url,
                              copr_package_url=copr_package_url,
                              releases_url=releases_url,
                              downloads_url=downloads_url,
                              s3_bucket_url=s3_bucket_url,
                              datetime_parse=parse,
                              num_monthly_orders=num_monthly_orders,
                              monthly_earning=monthly_earning,
                              monthly_earning_str=monthly_earning_str,
                              prev_month_earning_str=prev_month_earning_str,
                              prev_month_comparison_perc=prev_month_comparison_perc,
                              feature_tracker=feature_tracker,
                              bug_tracker=bug_tracker,
                              plugins=plugins,
                              feature_groups=feature_groups,
                              version=version,
                              pronunciation=pronunciation,
                              self_localized=self_localized,
                              url_localized=url_localized,
                              svg_localized=svg_localized,
                              screenshot=screenshot,
                              filename=name + "." + ext)
        out_name = "./rendered/" + locale + "/" + in_file.replace('template/', '').rstrip(".j2")
        os.makedirs("./rendered/" + locale, exist_ok=True)
        with codecs.open(out_name, "w", encoding='utf-8') as f:
            f.write(content)
