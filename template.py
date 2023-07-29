#!/usr/bin/env python3
# coding: utf-8
#
# Copyright (C) 2019-2023 Alexandros Theodotou <alex at zrythm dot org>
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
    'ca': ['🇪🇸', 'Català', 'EUR'],
    'cs': ['🇨🇿', 'Czech', 'EUR'],
    'da': ['🇩🇰', 'Dansk', 'EUR'],
    'de': ['🇩🇪', 'Deutsch', 'EUR'],
    'en': ['🇺🇸', 'English US', 'USD'],
    'en_GB': ['🇬🇧', 'English UK', 'GBP'],
    'el': ['🇬🇷', 'Ελληνικά', 'EUR'],
    'es': ['🇪🇸', 'Español', 'EUR'],
    #'et': ['🇪🇪', 'Eeti', 'EUR'],
    #'fi': ['🇫🇮', 'Suomi', 'EUR'],
    'fr': ['🇫🇷', 'Français', 'EUR'],
    #'gd': ['🏴󠁧󠁢󠁳󠁣󠁴󠁿', 'Gaelic', 'GBP'],
    'gl': ['🇪🇸', 'Galego', 'EUR'],
    'he': ['🇮🇱', 'עִבְרִית', 'USD'],
    'hi': ['🇮🇳', 'हिन्दी', 'USD'],
    'hu': ['🇭🇺', 'magyar nyelv', 'EUR'],
    'id': ['🇮🇩', 'bahasa Indonesia', 'USD'],
    'it': ['🇮🇹', 'Italiano', 'EUR'],
    'ja': ['🇯🇵', '日本語', 'JPY'],
    'ko': ['🇰🇷', '한국어', 'USD'],
    'mk': ['🇲🇰', 'македонски', 'EUR'],
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
forex_url = 'https://open.er-api.com/v6/latest/JPY'
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

# fetch products
single_price = float(0)
bundle_price = float(0)
subscription_price = float(0)
if fetch_orders:
    products_url = 'https://accounts.zrythm.org/api/v1/products/'
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
    print ('getting zrythm-accounts products...')
    r = requests.get(products_url, params=payload, headers=headers)
    if r.status_code == 200:
        for product in r.json()['results']:
            if product['type'] == 'Single':
                single_price = float(product['price_jpy'])
                break;
        for product in r.json()['results']:
            if product['type'] == 'Bundle':
                bundle_price = float(product['price_jpy'])
            elif product['type'] == 'Subscription':
                subscription_price = float(product['price_jpy'])

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
            amount = float (product['price_jpy'])
            amount -= (amount * 0.05)
            print ('adding {} zrythm accounts earnings (Order {})'.format(amount, order['id']))
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
                if 'transaction_subject' in tx and tx['transaction_subject'] == 'Subscription':
                    amount = float(tx['transaction_amount']['value'])
                    if 'fee_amound' in tx:
                        amount += float(tx['fee_amount']['value'])
                    if tx['transaction_amount']['currency_code'] == 'USD':
                        amount = amount / currency_rates['USD']
                    elif tx['transaction_amount']['currency_code'] == 'GBP':
                        amount = amount / currency_rates['GBP']
                    if amount > 0:
                        print ('adding {} paypal subscription earnings'.format(amount))
                        monthly_earning += amount
                elif 'invoice_id' not in tx and tx['transaction_event_code'] == 'T0000':
                    amount = float(tx['transaction_amount']['value'])
                    if 'fee_amound' in tx:
                        amount += float(tx['fee_amount']['value'])
                    if tx['transaction_amount']['currency_code'] == 'USD':
                        amount = amount / currency_rates['USD']
                    elif tx['transaction_amount']['currency_code'] == 'EUR':
                        amount = amount / currency_rates['EUR']
                    elif tx['transaction_amount']['currency_code'] == 'GBP':
                        amount = amount / currency_rates['GBP']
                    if amount > 0:
                        print ('adding {} paypal custom donation earnings'.format(amount))
                        monthly_earning += amount
        else:
            print (r.json())
    else:
        print (r.json())

# get liberapay earnings
    for lp_account in [ 'alextee' ]:
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
print ('monthly earning amt: {}'.format (monthly_earning_str))
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
    check_url (downloads_url + 'zrythm-trial-' + version + '-x86_64.flatpak')
    check_url (downloads_url + 'zrythm-trial-' + version + '-installer.zip')
    check_url (downloads_url + 'zrythm-trial-' + version + '-ms-setup.exe')
    check_url (downloads_url + 'zrythm-trial-' + version + '-osx-installer.zip')
    print ('done')

def url(x):
    # TODO: look at the app root environment variable
    # TODO: check if file exists
    return "../" + x

screenshot = url('static/images/screenshots/screenshot-20221015.png')
logo = url('static/icons/zrythm/z_frame_8.svg')
logo_png = url('static/icons/zrythm/z_frame_8.png')

class Plugin:
    def __init__(self,name,img,summary,features):
        self.name = name
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

        # global
        keywords = _('DAW, digital audio workstation, music production, audio, pro audio, Linux, GNU/Linux, free software, libre software, sound editor, composition, MIDI, LV2, JACK, VST, audio plugin, recording, editing, arrange, arranger, mixing, mastering')
        slogan = _('A highly automated and intuitive digital audio workstation.')

        # plugins
        basic_plugins = [
            Plugin(
                'Compressor', 'compressor.png',
                _('Stereo dynamic range compressor'), None),
            Plugin(
                'Cubic Distortion', 'cubic-distortion.png',
                _('Cubic nonlinearity distortion'), None),
            Plugin(
                'Flanger', 'flanger.png',
                _('Stereo flanging effect'), None),
            Plugin(
                'Gate Stereo', 'gate-stereo.png',
                _('Stereo signal gate'), None),
            Plugin(
                'Highpass Filter', 'highpass-filter.png',
                _('2nd-order Butterworth highpass filter'), None),
            Plugin(
                'Lowpass Filter', 'lowpass-filter.png',
                _('2nd-order Butterworth lowpass filter'), None),
            Plugin(
                'Parametric EQ', 'parametric-eq.png',
                _('Parametric equalizer'), None),
            Plugin(
                'Peak Limiter', 'peak-limiter.png',
                _('Dynamic range compressor modelled after the 1176 peak limiter'), None),
            Plugin(
                'Phaser', 'phaser.png',
                _('Phasing effect'), None),
            Plugin(
                'Triple Synth', 'triple-synth.png',
                _('Polyphonic synthesizer with 3 detuned oscillator voices'), None),
            Plugin(
                'Smooth Delay', 'smooth-delay.png',
                _("Delay that doesn't click and doesn't transpose when the delay time is changed"), None),
            Plugin(
                'Wah4', 'wah4.png',
                _('Wah pedal effect to the 4th order'), None),
            Plugin(
                'White Noise', 'white-noise.png',
                _('White noise generator'), None),
            Plugin(
                'Zita Rev1', 'zita-rev1.png',
                _('8x8 late-reverberation FDN reverb'), None),
            ]
        z_plugins = [
            Plugin(
                'ZChordz', 'zchordz.png',
                _('ZChordz maps the chords of a minor or major scale to white keys'),
                [ _('Major or minor scale'),
                    _('Velocity multiplier per note') ]),
            Plugin(
                'ZLFO', 'zlfo.png',
                _('ZLFO is a fully featured LFO for CV-based automation'),
                [ _('Multi-oscillator with custom wave'),
                    _('Phase shift'),
                    _('Vertical/horizontal inversion'),
                    _('Step mode'),
                    _('Editable range'),
                    _('Sync to host or free-form') ]),
            Plugin(
                'ZSaw', 'zsaw.png',
                _('ZSaw is a supersaw synth with 1 parameter'),
                [ _('7 sawtooth oscillators'),
                    _('Single knob to control detune') ]),
            ]

        def get_manual_ref(_manual_url):
            return '<a href="https://manual.zrythm.org/' + locale + '/' + _manual_url + '">'

        endref = '</a>'

        # features
        feature_groups = [
            FeatureGroup(
                _('Intuitive Editing'),
                [
                    Feature(
                        _('Flexible Select Tool'), 'piano-roll.gif',
                        _('Select, move, resize, clone, link, loop, delete and cut objects with a {ref}single tool{endref}.').format (ref = get_manual_ref ('editing/edit-tools.html#select-stretch-tool'), endref = endref)),
                    Feature(
                        _('Extensive Toolbox'), 'https://manual.zrythm.org/en/_images/toolbox.png',
                        _('Extend select tool functionality by switching to the {ref}Edit, Cut, Erase, Ramp or Audition tools{endref}.').format (ref = get_manual_ref ('editing/edit-tools.html#edit-tool'), endref = endref)),
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
                        _('Add multiple layers of audio/MIDI to the same track using {ref}track lanes{endref}.').format (ref = get_manual_ref ('tracks/track-lanes.html'), endref = endref)),
                    Feature(
                        _('Bounce in Place'), 'bounce-in-place.gif',
                        _('Quickly bounce selected material to audio.')),
                    Feature(
                        _('Stretching'), 'stretch-regions.gif',
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
                        _('Editor Functions'), 'audio-fade-out.gif',
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
                        _('Monitor Section'), 'https://manual.zrythm.org/en/_images/monitor-section.png',
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
                        _('Thanks to {ref}Carla{endref}, Zrythm supports a variety of plugin formats including LV2, VST2, VST3, AU, CLAP and JSFX.').format (ref = '<a href="https://github.com/falkTX/Carla/">', endref = endref)),
                    Feature(
                        _('SoundFonts as Plugins'), 'Sfz_file_format_logo.png',
                        _('Use SFZ and SF2 soundfonts as instrument plugins.')),
                    Feature(
                        _('Flexible Plugin Browser'), 'https://manual.zrythm.org/en/_images/plugin-browser.png',
                        _('Easily filter plugins by author, format or category, and organize your favorite plugins with plugin collections.')),
                    Feature(
                        _('Plugin Bridging'), 'https://manual.zrythm.org/en/_images/open-plugin-bridged.png',
                        _('Sandbox plugins by opening them in bridge mode.')),
                    Feature(
                        _('Automatable Bypass Mode'), 'automatable-plugin-enabled.png',
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
                        _('Import or export any format supported by {ref}libsndfile{endref}, with additional MP3 import support.').format (ref = '<a href="https://github.com/libsndfile/libsndfile">', endref = endref)),
                    Feature(
                        _('MIDI'), 'file-browser-midi-files.png',
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
                        _('Chord Presets'), 'https://manual.zrythm.org/en/_images/chord-preset-selection.png',
                        _('Generate chords from a wide range of scales, load included chord presets for various genres, or save your own.')),
                ]),
            FeatureGroup(
                _('Never Lose Work'),
                [
                    Feature(
                        _('Project Backups'), 'backup-saved-notification.png',
                        _('Backups taken automatically at user-specified intervals.')),
                    Feature(
                        _('Undoable Actions'), 'https://manual.zrythm.org/en/_images/undo-multiple.png',
                        _('Almost every user action is undoable.')),
                    Feature(
                        _('Serializable Undo History'), 'https://manual.zrythm.org/en/_images/undo-multiple.png',
                        _('Keep your undo history when saving projects.')),
                ]),
            FeatureGroup(
                _('Scripting'),
                [
                    Feature(
                        _('Extend Zrythm'), 'https://manual.zrythm.org/en/_images/scripting-interface.png',
                        _('Extend the capabilities of Zrythm by editing its state using {ref}GNU Guile scripts{endref}.').format (ref = get_manual_ref ('scripting/overview.html'), endref = endref)),
                    Feature(
                        _('Custom Editor Functions'), 'https://manual.zrythm.org/en/_images/scripting-interface.png',
                        _('Implement your own MIDI/audio/automation functions (coming soon).')),
                    Feature(
                        _('Project Generation'), 'https://manual.zrythm.org/en/_images/scripting-interface.png',
                        _('Generate projects with GNU Guile scripts.')),
                ]),
            FeatureGroup(
                _('Optimized Performance'),
                [
                    Feature(
                        _('Hardware accelerated UI'), 'https://manual.zrythm.org/en/_images/first-run-interface.png',
                        _('Most of the user interface is drawn on the GPU thanks to {ref}GTK4{endref}.').format (ref = '<a href="https://gtk.org/">', endref = endref)),
                    Feature(
                        _('SIMD-optimized DSP'), 'LSP_logo_hover.png',
                        _('Zrythm uses {ref}lsp-dsp-lib{endref} which implements SIMD extensions such as SSE, AVX and FMA when available to speed up audio processing and minimize DSP usage.').format (ref = '<a href="https://github.com/lsp-plugins/lsp-dsp-lib">', endref = endref)),
                    Feature(
                        _('Extensive Caching'), 'xfce4-cpugraph-plugin.svg',
                        _('Expensive computations are pre-calculated to save processing time.')),
                ]),
            FeatureGroup(
                _('Cross-Platform Support'),
                [
                    Feature(
                        _('Multiple Platforms'), 'piano-roll.gif',
                        _('Zrythm is designed to run on a {ref}wide variety of platforms and architectures{endref} including x86 architectures, PowerPC, RISC-V, ARMv7 and ARMv8.').format (ref = get_manual_ref ('getting-started/system-requirements.html'), endref = endref)),
                    Feature(
                        _('Multiple Backends'), 'audio-backend-selection.png',
                        _('Support for almost all major audio and MIDI backends, including JACK/PipeWire, Windows MME, WASAPI and Core Audio/MIDI.')),
                ]),
            FeatureGroup(
                _('Localization'),
                [
                    Feature(
                        _('Localized UI'), 'localized-ui.png',
                        _('Use Zrythm in your preferred language.')),
                    Feature(
                        _('Easily Add Translations'), 'weblate-logo-darktext-borders.png',
                        _('Add missing translations and locales on {ref}Weblate{endref}.').format (ref = '<a href="https://hosted.weblate.org/engage/zrythm/">', endref = endref)),
                ]),
            FeatureGroup(
                _('User Freedom'),
                [
                    Feature(
                        _('Free Software'), 'programming.png',
                        _('All source code is released as {ref}copyleft free software{endref}.').format (ref = '<a href="https://www.gnu.org/licenses/copyleft.en.html">', endref = endref)),
                    Feature(
                        _('Open Standards'), 'FLAC_logo_vector.svg',
                        _('Zrythm supports open standards such as MIDI, LV2, FLAC and OGG.')),
                    Feature(
                        _('Cooperation'), 'gnu-and-penguin-color-1024x946-trnsprnt.png',
                        _('We work with the free software community to ensure Zrythm builds and runs without issues on all platforms.')),
                ]),
            ]

        # highlights
        highlights = [
            Feature(
                _('Intuitive Editing'), 'piano-roll.gif',
                _('Easily select, move, resize, clone, link, loop, delete and cut objects with a single tool or extend its functionality with additional specialized tools, and enjoy adaptive snapping in every arranger.')),
            Feature(
                _('Limitless Automation'), 'automation-curves.gif',
                _('Automate almost anything with automation events using straight lines, ramps and curves, or with LFOs and envelopes.')),
            Feature(
                _('Mixing Capabilities'), 'https://manual.zrythm.org/en/_images/mixer.png',
                _('In-context listening, signal groups, FX tracks, MIDI effect and insert slots, pre and post-fader aux sends and anywhere-to-anywhere routing.')),
            Feature(
                _('Chord Assistance'), 'chord-highlighting.png',
                _('Generate chords from scales in the chord pad, audition and invert chords or save your own chord presets, manage your chord progression in the chord track and enjoy chord highlighting in the piano roll.')),
            Feature(
                _('Audio Plugins'), 'plugin-showcase.png',
                _('Support for every major plugin format including {lv2_ref}LV2{endref}, VST2, VST3, AU, CLAP and JSFX, with additional support for SFZ and SF2 soundfonts and sandboxing thanks to {carla_ref}Carla{endref}.').format (lv2_ref = '<a href="https://lv2plug.in/">', carla_ref = '<a href="https://kx.studio/Applications:Carla">', endref = '</a>')),
            Feature(
                _('Featureful Timeline'), 'https://manual.zrythm.org/en/_images/track-lanes.png',
                _('Organize your work into multiple layers in the same track using track lanes, quickly bounce anything to audio, import/export a wide variety of audio and MIDI formats, stretch or loop any region and select from an array of track types for every purpose.')),
            Feature(
                _('Never Lose Work'), 'https://manual.zrythm.org/en/_images/undo-multiple.png',
                _('Recover your work with automatic project backups, undo almost any user action and even save your undo history with projects.')),
            Feature(
                _('Liberating'), 'programming.png',
                _('Zrythm is {copyleft_ref}copyleft{endref} {free_software_ref}free software</a> with fully auditable source code. Use, study, share and improve it freely.').format (copyleft_ref = '<a href="https://en.wikipedia.org/wiki/Copyleft">', free_software_ref = '<a href="https://www.zrythm.org/videos/TEDxGE2014_Stallman05_LQ.webm">', endref = '</a>')),
            ]

        currency_for_locale = langs_full[locale][2]
        currency_sym_for_locale = currency_symbols[currency_for_locale]
        single_price_for_locale = round (single_price * currency_rates[currency_for_locale])
        bundle_price_for_locale = round (bundle_price * currency_rates[currency_for_locale])
        subscription_price_for_locale = round (subscription_price * currency_rates[currency_for_locale])
        monthly_earning_for_locale = round (monthly_earning * currency_rates[currency_for_locale])
        local_salary_for_locale = round (2625 * currency_rates[currency_for_locale])
        # if JPY, round again to 100s
        if currency_for_locale == 'JPY' or currency_for_locale == 'RUB':
            single_price_for_locale = round (single_price_for_locale, -2)
            bundle_price_for_locale = round (bundle_price_for_locale, -2)
            subscription_price_for_locale = round (subscription_price_for_locale, -2)
            monthly_earning_for_locale = round (monthly_earning_for_locale, -2)
            local_salary_for_locale = round (local_salary_for_locale, -2)
        single_price_for_locale = '{}{:,}'.format (currency_sym_for_locale, single_price_for_locale)
        bundle_price_for_locale = '{}{:,}'.format (currency_sym_for_locale, bundle_price_for_locale)
        subscription_price_for_locale = '{}{:,}'.format (currency_sym_for_locale, subscription_price_for_locale)
        monthly_earning_str = '{}{:,}'.format (currency_sym_for_locale, monthly_earning_for_locale)
        local_salary_str = '{}{:,}'.format (currency_sym_for_locale, local_salary_for_locale)

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
                              local_salary_str=local_salary_str,
                              prev_month_earning_str=prev_month_earning_str,
                              prev_month_comparison_perc=prev_month_comparison_perc,
                              feature_tracker=feature_tracker,
                              bug_tracker=bug_tracker,
                              highlights=highlights,
                              basic_plugins=basic_plugins,
                              z_plugins=z_plugins,
                              feature_groups=feature_groups,
                              version=version,
                              pronunciation=pronunciation,
                              self_localized=self_localized,
                              url_localized=url_localized,
                              svg_localized=svg_localized,
                              screenshot=screenshot,
                              keywords=keywords,
                              logo=logo,
                              logo_png=logo_png,
                              slogan=slogan,
                              filename=name + "." + ext)
        out_name = "./rendered/" + locale + "/" + in_file.replace('template/', '').rstrip(".j2")
        os.makedirs("./rendered/" + locale, exist_ok=True)
        with codecs.open(out_name, "w", encoding='utf-8') as f:
            f.write(content)
