<!--
  <div id="header" class="">
    <ul class="skip">
      <li><a href="#nav">jump to main navigation</a></li>
      <li><a href="#content">jump to main content</a></li>
      <li><a href="#footer">jump to footer</a></li>
    </ul>
  </div>
-->
<noscript>
  <style>
    .collapse
    {
    display: block;
    }
  </style>
</noscript>

<!-- <nav class="navbar navbar-toggleable navbar-toggleable-md navbar-expand-md navbar-inverse navbar-dark fixed-top bg-dark"> -->
<!--<nav class="navbar navbar-expand-md navar-inverse navbar-dark bg-dark fixed-top"> -->
<nav class="navbar navbar-expand-md fixed-top">
  <a class="navbar-brand" href="index.html">
    <!--
      TODO: imo this is bad in the navbar.
      a readable "gnunet" font-logo would
      be better for orientation.
      -->
      <img src="{{ url('static/images/z.svg') }}" alt="Zrythm Home Icon" />
  </a>

  <!-- menu button -->
  <button class="navbar-toggler navbar-toggler-right custom-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarMain"
          aria-controls="navbarMain"
          aria-expanded="false"
          aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
  </button>
  <!-- /menu button -->

  <!-- navbar -->
  <div class="collapse navbar-collapse" id="navbarMain">
    <ul class="navbar-nav mr-auto nav">
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown"
           role="button" aria-haspopup="true" aria-expanded="false">
           {{ _("Community") }}
        </a>
        <ul class="dropdown-menu" aria-labelledby="navbarMain">
          <li><a class="dropdown-item" href="https://forum.zrythm.org">{{ _("Forum") }} </a></li>
          <li><a class="dropdown-item" href="engage.html">{{ _("Discussion") }} </a></li>
          <li><a class="dropdown-item" href="join-us.html">{{ _("Join Us") }}</a></li>
        </ul>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarMain"
           data-toggle="dropdown" role="button"
           aria-haspopup="true" aria-expanded="false">
           {{ _("Development") }}
        </a>
        <ul class="dropdown-menu" aria-labelledby="navbarMain">
          <li><a class="dropdown-item" href="https://docs.zrythm.org">{{ _("Developer Docs") }}</a></li>
          <li><a class="dropdown-item" href="https://git.zrythm.org/zrythm/zrythm/issues">{{ _("Bug Tracker") }}</a></li>
          <li><a class="dropdown-item" href="https://git.zrythm.org/zrythm/zrythm">{{ _("Source Code") }}</a></li>
        </ul>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle"
           href="#"
           data-toggle="dropdown"
           role="button"
           aria-haspopup="true"
           aria-expanded="false">
           {{ _("Documentation") }}
        </a>
        <ul class="dropdown-menu" aria-labelledby="navbarMain">
          <li><a class="dropdown-item" href="tutorial.html">{{ _("Tutorials") }}</a></li>
                <li><a class="dropdown-item" href="https://manual.zrythm.org/introduction-to-zrythm/basic-concepts-and-terminology.html">{{ _("Glossary") }}</a></li>
          <li><a class="dropdown-item" target="_blank" href="https://manual.zrythm.org">{{ _("Manual") }}</a></li>
                <li><a class="dropdown-item" href="faq.html">{{ _("FAQ") }}</a></li>
        </ul>
      </li>
      <li class="nav-item badge">
        <a href="https://hosted.weblate.org/engage/zrythm/?utm_source=widget">
          <img src="https://hosted.weblate.org/widgets/zrythm/-/svg-badge.svg" alt="Translation status" />
        </a>
      </li>
      <li class="nav-item badge">
        <a href="https://git.zrythm.org/zrythm/zrythm/pipelines"><img src="https://git.zrythm.org/zrythm/zrythm/badges/master/pipeline.svg" alt="Pipeline"></img></a>
      </li>
      <li class="nav-item badge">
        <a href="https://git.zrythm.org/zrythm/zrythm"><img src="https://git.zrythm.org/zrythm/zrythm/badges/master/coverage.svg" alt="Coverage"></img></a>
      </li>
      <li class="nav-item badge">
        <a href="https://riot.im/app/#/room/#freenode_#zrythm:matrix.org?action=chat"><img src="https://git.zrythm.org/zrythm/zrythm/raw/master/data/chat-matrix.svg?inline=false" alt="Chat on Matrix"></img></a>
      </li>
      <li class="nav-item badge">
        <a href="https://liberapay.com/Zrythm"><img src="http://img.shields.io/liberapay/patrons/Zrythm.svg?logo=liberapay" alt="LiberaPay Patrons"></img></a>
      </li>
    </ul>
    <ul class="navbar-nav navbar-right nav">
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#"
           data-toggle="dropdown" role="button"
           aria-haspopup="true" aria-expanded="false">
           {{ lang_full }} {{ lang_flag }}
        </a>
        <ul class="dropdown-menu dropdown-menu-right scrollable-menu" aria-labelledby="navbarMain">
        {% for key in langs_full.keys() %}
          <li><a class="dropdown-item" href="{{ self_localized(key) }}">{{ lang_flags[key] }} {{ langs_full[key] }}</a></li>
        {% endfor %}
        </ul>
      </li> <!-- /navbar-right dropdown -->
    </ul> <!-- /navbar-right -->
  </div> <!-- /navbar -->
</nav>
