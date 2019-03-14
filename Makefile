# This file is in the public domain.

# All: build HTML pages in all languages and compile the
# TypeScript logic in web-common.

# Hardly anyone seems to read README files anymore, so keep this note here:
# Don't remove the variables for python etc. They exist
# because one system sticks with PEPs, and others opt
# for installing every version side-by-side,
# Same goes for babel.

include config.mk

all: locale template
	# Consider using pax instead of cp.
	cp -R dist rendered/
	cp -R static rendered/
	cp rendered/static/robots.txt rendered/robots.txt
	cp rendered/static/robots.txt rendered/dist/robots.txt
	cp rendered/static/robots.txt rendered/en/robots.txt
	cp rendered/static/robots.txt rendered/de/robots.txt
	cp rendered/static/robots.txt rendered/es/robots.txt
	cp rendered/static/robots.txt rendered/fr/robots.txt
	cp rendered/static/robots.txt rendered/it/robots.txt
	/bin/sh make_sitemap.sh
	cp rendered/sitemap.xml rendered/en/sitemap.xml
	cp rss.xml rendered/rss.xml
	cp rss.xml rendered/en/rss.xml
	cp rss.xml rendered/de/rss.xml
	cp rss.xml rendered/es/rss.xml
	cp rss.xml rendered/fr/rss.xml
	cp rss.xml rendered/it/rss.xml
	cp static/moved.html rendered/frontpage.html
	cd rendered; ln -fs frontpage.html frontpage

# Extract translateable strings from jinja2 templates.
# Because of the local i18nfix extractor module we need
# to set the pythonpath before invoking pybabel.
locale/messages.pot: common/*.j2.inc template/*.j2
	PYTHONPATH=. $(BABEL) -v extract -F locale/babel.map -o locale/messages.pot .

# Update translation (.po) files with new strings.
locale-update: locale/messages.pot
	msgmerge -U -m --previous locale/en/LC_MESSAGES/messages.po locale/messages.pot
	msgmerge -U -m --previous locale/de/LC_MESSAGES/messages.po locale/messages.pot
	msgmerge -U -m --previous locale/fr/LC_MESSAGES/messages.po locale/messages.pot
	msgmerge -U -m --previous locale/es/LC_MESSAGES/messages.po locale/messages.pot
	msgmerge -U -m --previous locale/it/LC_MESSAGES/messages.po locale/messages.pot

	if grep -nA1 '#-#-#-#-#' locale/*/LC_MESSAGES/messages.po; then echo -e "\nERROR: Conflicts encountered in PO files.\n"; exit 1; fi

# Compile translation files for use.
locale-compile:
	$(BABEL) -v compile -d locale -l en --use-fuzzy
	$(BABEL) -v compile -d locale -l de --use-fuzzy
	$(BABEL) -v compile -d locale -l fr --use-fuzzy
	$(BABEL) -v compile -d locale -l it --use-fuzzy
	$(BABEL) -v compile -d locale -l es --use-fuzzy

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
	rm -rf en/ de/ fr/ it/ es/ ru/
	rm -rf rendered/
	rm -rf *.pyc *~ \.*~ \#*\#
