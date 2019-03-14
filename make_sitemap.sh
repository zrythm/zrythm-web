#!/bin/sh

# This initial version builds on code from ssg4
# copyright is as follows:
# -----
# https://www.romanzolotarev.com/bin/ssg4
# Copyright 2018 Roman Zolotarev <hi@romanzolotarev.com>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
# -----

list_pages(){
cd rendered && find . -type f ! -path '*/.*' ! -path '*/_*' -name '*.html' | sed 's#^./##;#'
}

main(){
	dst=rendered
        base_url="$4"
        date=$(date +%Y-%m-%d)
        urls=$(list_pages "$src")

        test -n "$urls" &&
        render_sitemap "$urls" "$base_url" "$date" > "$dst/sitemap.xml"

        print_status 'url' 'urls' "$urls" >&2
        echo >&2
}

print_status() {
        test -z "$3" && printf 'no %s' "$2" && return

        echo "$3" | awk -v singular="$1" -v plural="$2" '
        END {
                if (NR==1) printf NR " " singular
                if (NR>1) printf NR " " plural
        }'
}

render_sitemap() {
        urls="$1"
        base_url="$2"
        date="$3"

        echo '<?xml version="1.0" encoding="UTF-8"?>'
        echo '<urlset'
        echo 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
        echo 'xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9'
        echo 'http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd"'
        echo 'xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        echo "$urls" |
        sed -E 's#^(.*)$#<url><loc>'"$base_url"'/\1</loc><lastmod>'\
"$date"'</lastmod><priority>1.0</priority></url>#'
        echo '</urlset>'
}

main "$@"

