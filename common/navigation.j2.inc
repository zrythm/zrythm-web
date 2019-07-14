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
      <img src="{{ url('static/images/z.svg') }}" alt="Zrythm Home Icon" height="24px" />
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
          <!--<li><a class="dropdown-item" href="https://forum.zrythm.org">{{ _("Forum") }} </a></li>-->
          <li><a class="dropdown-item" href="engage.html">{{ _("Discussion") }} </a></li>
          <li><a class="dropdown-item" href="join-us.html">{{ _("Join Us") }}</a></li>
        </ul>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle"
           href="#"
           data-toggle="dropdown"
           role="button"
           aria-haspopup="true"
           aria-expanded="false">
           {{ _("Development") }}
        </a>
        <ul class="dropdown-menu" aria-labelledby="navbarMain">
          <li><a class="dropdown-item" href="https://docs.zrythm.org">{{ _("Developer Docs") }}</a></li>
          <li><a class="dropdown-item" href="{{ issue_tracker }}">{{ _("Issue Tracker") }}</a></li>
          <li><a class="dropdown-item" href="{{ git_url }}">{{ _("Source Code") }}</a></li>
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
                <li><a class="dropdown-item" href="https://manual.zrythm.org/{{ lang }}/getting-started/basic-concepts-and-terminology.html">{{ _("Glossary") }}</a></li>
          <li><a class="dropdown-item" target="_blank" href="https://manual.zrythm.org/{{ lang }}/">{{ _("Manual") }}</a></li>
                <li><a class="dropdown-item" href="faq.html">{{ _("FAQ") }}</a></li>
        </ul>
      </li>
      <li class="nav-item badge">
        <a href="http://download.savannah.nongnu.org/releases/zrythm/">
          <img src="https://img.shields.io/badge/release-{{ version }}-blue.svg" alt="Release" />
        </a>
      </li>
      <li class="nav-item badge">
        <a href="https://hosted.weblate.org/engage/zrythm/?utm_source=widget">
          <img src="https://hosted.weblate.org/widgets/zrythm/-/svg-badge.svg" alt="Translation status" />
        </a>
      </li>
      <li class="nav-item badge">
        <a href="https://www.gnu.org/licenses/agpl-3.0.html">
          <img src="{{ url('static/images/agpl-v3.svg') }}" alt="License" height="35px" />
        </a>
      </li>
      <li class="nav-item badge">
        <a href="https://liberapay.com/Zrythm/donate"><img alt="Donate using Liberapay" src="{{ url('static/images/donate_liberapay.svg') }}"></a>
      </li>
    </ul>
    <ul class="navbar-nav navbar-right nav">
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#"
           data-toggle="dropdown" role="button"
           aria-haspopup="true" aria-expanded="false">
           <i class="fa fa-language" aria-hidden="true"></i> {{ lang_full }} {{ lang_flag }}
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
