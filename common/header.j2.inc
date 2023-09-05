{#
Copyright (C) 2019-2021 Alexandros Theodotou <alex at zrythm dot org>

This file is part of Zrythm

Zrythm is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Zrythm is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
#}

<meta charset="UTF-8"/>
{% for key in langs_full.keys() %}
<link rel="alternate" hreflang="{{ key }}" href="{{ self_localized(key) }}" />
{% endfor %}

<!-- OpenGraph -->
<meta name="og:title" content="Zrythm DAW">
<meta property="og:description" content="{{ slogan }}" />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://www.zrythm.org/en/index.html" />
<meta property="og:image" content="{{ screenshot }}" />

<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="author" content="Alexandros Theodotou">
<meta name="keywords" content="{{ keywords }}">
<link rel="icon" href="{{ url('static/favicon.ico') }}">

<!-- Custom styles for this template -->
<link href="{{ url('static/styles.css?v=202203302022') }}" rel="stylesheet">

<!-- Umami -->
<script async src="https://analytics.zrythm.org/script.js" data-website-id="3ce24de1-a63b-4094-a9a3-887edfc2238f"></script>
