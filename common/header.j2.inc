{#
Copyright (C) 2019 Alexandros Theodotou <alex at zrythm dot org>

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

<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="author" content="Alexandros Theodotou">
<meta name="keywords" content="{{ _('DAW, digital audio workstation, music production, audio, pro audio, Linux, GNU/Linux, free software, libre software, sound editor, composition, MIDI, LV2, JACK') }}">
<link rel="icon" href="{{ url('static/favicon.ico') }}">

<!-- mini.css -->
<link href="{{ url('dist/mini.css/mini-dark.css') }}" rel="stylesheet">

<!-- Custom styles for this template -->
<link href="{{ url('static/styles.css') }}" rel="stylesheet">
