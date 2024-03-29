#
# Copyright (C) 2019-2022 Alexandros Theodotou <alex at zrythm dot org>
# Copyright (C) 2017, 2018, 2019 GNUnet e.V.
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.
#
# ----

# All: build HTML pages in all languages and compile the
# TypeScript logic in web-common.

# Hardly anyone seems to read README files anymore, so keep this note here:
# Don't remove the variables for python etc. They exist
# because one system sticks with PEPs, and others opt
# for installing every version side-by-side,
# Same goes for babel.

include config.mk

LANGUAGES = af_ZA ar ca en en_GB gd de es el fr gl he id it mk nl ja pt pt_BR ru hi hu ko nb_NO cs pl da et fi sl sv th tr uk vi zh_CN zh_TW

all: locale/messages.pot locale template
	# Consider using pax instead of cp.
	cp -R dist rendered/
	cp -R static rendered/
	cp -R static-unprefixed/* rendered/
	/bin/sh make_sitemap.sh
	cp rendered/sitemap.xml rendered/en/sitemap.xml
	#cp rss.xml rendered/rss.xml
	#for lang in $(LANGUAGES); do \
		#cp rss.xml rendered/$$lang/rss.xml ; \
	#done

# Extract translateable strings from jinja2 templates.
# Because of the local i18nfix extractor module we need
# to set the pythonpath before invoking pybabel.
locale/messages.pot: common/*.j2.inc template/*.j2 template.py
	PYTHONPATH="${PYTHONPATH}:." $(BABEL) -v extract -F locale/babel.map -o locale/messages.pot .

# Update or create translation (.po) files with new strings.
locale-update: locale/messages.pot
	for lang in $(LANGUAGES); do \
		if [[ "x$$lang" != "xen" ]] ; then \
			po_file_basedir=locale/$$lang/LC_MESSAGES ; \
			po_file=$$po_file_basedir/messages.po ; \
			if [ ! -f "$$po_file" ]; then \
				$(BABEL) -v init -i locale/messages.pot -d locale -l $$lang ; \
			fi ; \
			msgmerge -U -m --previous "$$po_file" locale/messages.pot ; \
		fi \
	done

	if grep -nA1 '#-#-#-#-#' locale/*/LC_MESSAGES/messages.po; then echo -e "\nERROR: Conflicts encountered in PO files.\n"; exit 1; fi

# Compile translation files for use.
locale-compile:
	for lang in $(LANGUAGES); do \
		if [[ "x$$lang" != "xen" ]] ; then \
			$(BABEL) -v compile -d locale -l $$lang ; \
		fi \
	done

# Process everything related to gettext translations.
locale: locale-update locale-compile

# Run the jinja2 templating engine to expand templates to HTML
# incorporating translations.
template: locale-compile .credentials template/styles.scss
	. ./.credentials && \
	$(PYTHON) ./template.py && \
	sass --sourcemap=none template/styles.scss static/styles.css

it: template

current_dir = $(shell pwd)

run: all
	@[ "$(BROWSER)" ] || ( echo "You need to export the environment variable 'BROWSER' to run this."; exit 1 )
	$(RUN_BROWSER) http://0.0.0.0:8000 &
	cd rendered && $(PYTHON) -m http.server

clean:
	rm -rf __pycache__
	rm -rf rendered/
	rm -rf *.pyc *~ \.*~ \#*\#
