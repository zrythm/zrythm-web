# This file is licensed under CC0 1.0.
# <https://creativecommons.org/publicdomain/zero/1.0/>

# All: build HTML pages in all languages and compile the
# TypeScript logic in web-common.

# Hardly anyone seems to read README files anymore, so keep this note here:
# Don't remove the variables for python etc. They exist
# because one system sticks with PEPs, and others opt
# for installing every version side-by-side,
# Same goes for babel.

include config.mk

LANGUAGES = en gd de es el fr it nl ja pt pt_BR ru zh hi ar ko nb_NO cs pl da et fi sv

all: locale/messages.pot locale template
	# Consider using pax instead of cp.
	cp -R dist rendered/
	cp -R static rendered/
	cp rendered/static/robots.txt rendered/robots.txt
	cp rendered/static/robots.txt rendered/dist/robots.txt
	for lang in $(LANGUAGES); do \
		cp rendered/static/robots.txt rendered/$$lang/robots.txt; \
	done
	/bin/sh make_sitemap.sh
	cp rendered/sitemap.xml rendered/en/sitemap.xml
	#cp rss.xml rendered/rss.xml
	#for lang in $(LANGUAGES); do \
		#cp rss.xml rendered/$$lang/rss.xml ; \
	#done

# Extract translateable strings from jinja2 templates.
# Because of the local i18nfix extractor module we need
# to set the pythonpath before invoking pybabel.
locale/messages.pot: common/*.j2.inc template/*.j2
	PYTHONPATH=. $(BABEL) -v extract -F locale/babel.map -o locale/messages.pot .

# Update translation (.po) files with new strings.
locale-update: locale/messages.pot
	for lang in $(LANGUAGES); do \
		msgmerge -U -m --previous locale/$$lang/LC_MESSAGES/messages.po locale/messages.pot ; \
	done

	if grep -nA1 '#-#-#-#-#' locale/*/LC_MESSAGES/messages.po; then echo -e "\nERROR: Conflicts encountered in PO files.\n"; exit 1; fi

# Compile translation files for use.
locale-compile:
	for lang in $(LANGUAGES); do \
		$(BABEL) -v compile -d locale -l $$lang --use-fuzzy ; \
	done

# Process everything related to gettext translations.
locale: locale-update locale-compile

# Run the jinja2 templating engine to expand templates to HTML
# incorporating translations.
template: locale-compile
	$(PYTHON) ./template.py

it: template

current_dir = $(shell pwd)

run: all
	@[ "$(BROWSER)" ] || ( echo "You need to export the environment variable 'BROWSER' to run this."; exit 1 )
	$(RUN_BROWSER) http://0.0.0.0:8000 &
	cd rendered && $(PYTHON) -m http.server


# docker-all: Build using a docker image which contains all the needed packages.

docker: docker-all

docker-all:
	docker build -t gnunet-www-builder .
	# Importing via the shell like this is hacky,
	# but after trying lots of other ways, this works most reliably...
	$(PYTHON) -c 'import i18nfix'
	docker run --rm -v $$(pwd):/tmp/ --user $$(id -u):$$(id -g) gnunet-www-builder

clean:
	rm -rf __pycache__
	rm -rf en/ de/ fr/ it/ es/ ru/ zh/ pt/
	rm -rf rendered/
	rm -rf *.pyc *~ \.*~ \#*\#
