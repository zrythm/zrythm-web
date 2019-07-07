    <script>
        /*
        @licstart  The following is the entire license notice for the
        JavaScript code in this page.

        Copyright (C) 2019 Alexandros Theodotou
        Copyright (C) 2014-2017 GNUnet e.V.

        The JavaScript code in this page is free software: you can
        redistribute it and/or modify it under the terms of the GNU
        General Public License (GNU GPL) as published by the Free Software
        Foundation, either version 3 of the License, or (at your option)
        any later version.  The code is distributed WITHOUT ANY WARRANTY;
        without even the implied warranty of MERCHANTABILITY or FITNESS
        FOR A PARTICULAR PURPOSE.  See the GNU GPL for more details.

        As additional permission under GNU GPL version 3 section 7, you
        may distribute non-source (e.g., minimized or compacted) forms of
        that code without the copy of the GNU GPL normally required by
        section 4, provided you include this license notice and a URL
        through which recipients can access the Corresponding Source.

        @licend  The above is the entire license notice
        for the JavaScript code in this page.
        */
    </script>

    <link rel="alternate" hreflang="en" href="{{ self_localized('en') }}" />
    <link rel="alternate" hreflang="de" href="{{ self_localized('de') }}" />
    <link rel="alternate" hreflang="fr" href="{{ self_localized('fr') }}" />
    <link rel="alternate" hreflang="es" href="{{ self_localized('es') }}" />
    <link rel="alternate" hreflang="it" href="{{ self_localized('it') }}" />

    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="author" content="Zrythm contributors">
    <link rel="icon" href="{{ url('static/favicon.ico') }}">

    <!-- Bootstrap core CSS -->
    <link href="{{ url('dist/css/bootstrap.min.css') }}" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="{{ url('static/styles.css') }}" rel="stylesheet">

    <script src="{{ url('dist/js/jquery-1.11.1.min.js') }}"></script>
    <script src="{{ url('dist/js/bootstrap.min.js') }}"></script>
    <link href="{{ url('static/navbar.css') }}" rel="stylesheet">

    <!-- Responsiveslides JS/CSS -->
    <script src="{{ url('dist/js/responsiveslides.min.js') }}"></script>
    <link href="{{ url('static/responsiveslides.css') }}" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
    <!-- fork awesome, for team page -->
    <link href="{{ url('dist/font-awesome/css/all.css') }}" rel="stylesheet">
    <link href="{{ url('dist/fork-awesome/css/fork-awesome.min.css') }}" rel="stylesheet">
    <!-- <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/fork-awesome@1.1.7/css/fork-awesome.min.css" integrity="sha256-gsmEoJAws/Kd3CjuOQzLie5Q3yshhvmo7YNtBG7aaEY=" crossorigin="anonymous"> -->

    <!-- handwritten rss -->
    <link rel="alternate" type="application/rss+xml" title="Zrythm.org rss" href="rss.xml" />

    <!-- rss and atom, WIP
    <link rel="alternate" type="application/rss+xml" href="{{ url('feed.rss') }} title="RSS feed for zrythm.org">
    <link rel="alternate" type="application/atom+xml" href="{{ url('feed.atom') }} title="Atom feed for zrythm.org">
    -->
