{#
Copyright (C) 2023-2024 Alexandros Theodotou <alex at zrythm dot org>
Copyright (C) 2022 Andrew Harter <andrewhharter@gmail.com>

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

<footer class="footer__container">
  <div class="container">
    <div class="footer__section footer__section--copyright">
      <a href="{{ url(lang + '/index.html') }}" class="footer__logo">
        <img class="footer__image" src="{{ url('static/icons/zrythm/z_frame_8.svg') }}">
        <p class="footer__logo--text">Zrythm DAW</p>
      </a>
      <p>&copy; 2019-2025, The Zrythm contributors.</p>
      <p>{{ _('Zrythm and the Zrythm logo are {ref}trademarks of Alexandros Theodotou{endref}.').format (
        ref = '<a href="{{ git_url }}/-/blob/master/TRADEMARKS.md">', endref = '</a>') }}</p>
    </div>
    <div class="footer__section">
      <h4 class="footer__title">{{ _('Project') }}</h4>
      <ul class="footer__links">
        <li class="footer__link">
          <a href="{{ url(lang + '/features.html') }}">{{ _('Features') }}</a>
        </li>
        <li class="footer__link">
          <a href="https://manual.zrythm.org/{{ lang }}/index.html">{{ _('User Manual') }}</a>
        </li>
        <li class="footer__link">
          <a href="https://www.zrythm.org/releases">{{ _('Releases') }}</a>
        </li>
        <li class="footer__link">
          <a href="{{ git_url }}">{{ _('Git') }}</a>
        </li>
      </ul>
    </div>
    <div class="footer__section">
      <h4 class="footer__title">{{ _('Community') }}</h4>
      <ul class="footer__links">
        <li class="footer__link">
          <a href="https://matrix.to/#/#zrythmdaw:matrix.org">{{ _('Chat') }}</a>
        </li>
        <li class="footer__link">
          <a href="{{ forum_url }}">{{ _('Forum') }}</a>
        </li>
        <li class="footer__link">
          <a href="{{ url(lang + '/community.html#contribute') }}">{{ _('Contribute') }}</a>
        </li>
        <li class="footer__link">
          <a href="{{ url(lang + '/community.html#donate') }}">{{ _('Donate') }}</a>
        </li>
      </ul>
    </div>
    <div class="footer__section">
      <h4 class="footer__title footer__title--bold">{{ _('About this Site') }}</h4>
      <ul class="footer__links">
        <li class="footer__link">
          <a href="https://gitlab.zrythm.org/zrythm/zrythm-web">{{ _('Source Code') }}</a>
        </li>
        <li class="footer__link">
          <a href="{{ url(lang + '/legal.html') }}">{{ _('Legal Information') }}</a>
        </li>
        <li class="footer__link">
          <a href="{{ url(lang + '/privacy.html') }}">{{ _('Privacy Policy') }}</a>
        </li>
        <li class="footer__link">
          <a href="https://gitlab.zrythm.org/zrythm/zrythm-web/-/issues">{{ _('Report an Issue') }}</a>
        </li>
        <li class="footer__link">
          <p>{{ _('Designed by Andrew Harter') }}</p>
        </li>
      </ul>
    </div>
  </div>
</footer>
