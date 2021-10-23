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
<meta property="og:description" content="{{ _('A highly automated and intuitive digital audio workstation.') }}" />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://www.zrythm.org/en/index.html" />
<meta property="og:image" content="{{ screenshot }}" />

<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="author" content="Alexandros Theodotou">
<meta name="keywords" content="{{ _('DAW, digital audio workstation, music production, audio, pro audio, Linux, GNU/Linux, free software, libre software, sound editor, composition, MIDI, LV2, JACK, VST, audio plugin, recording, editing, arrange, arranger, mixing, mastering') }}">
<link rel="icon" href="{{ url('static/favicon.ico') }}">

<!-- mini.css -->
{#<link href="{{ url('dist/mini.css/mini-dark.css') }}" rel="stylesheet">#}

<!-- Custom styles for this template -->
<link href="{{ url('static/styles.css?v=20211024') }}" rel="stylesheet">

<!-- Matomo -->
<script type="text/javascript">
  var _paq = window._paq = window._paq || [];
  /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
  _paq.push(["setDoNotTrack", true]);
  _paq.push(["setDomains", ["*.www.zrythm.org"]]);
  _paq.push(["disableCookies"]);
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="https://matomo.zrythm.org/";
    _paq.push(['setTrackerUrl', u+'matomo.php']);
    _paq.push(['setSiteId', '1']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript'; g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
  })();
</script>
<noscript><img src="https://matomo.zrythm.org/matomo.php?idsite=1&amp;rec=1" style="border:0;" alt="" /></noscript>
<!-- End Matomo Code -->
