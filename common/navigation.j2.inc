{#
Copyright (C) 2019-2021 Alexandros Theodotou <alex at zrythm dot org>
Copyright (C) 2021 Andrew Harter <andrewhharter@gmail.com>

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

<header class="navbar">
    <div class="container navbar__content">
        <a href="{{ url(lang + '/index.html') }}" class="navbar__logo">
            <img class="navbar__image" src="{{ url('static/icons/zrythm/z_frame_8.svg') }}">
        </a>
        <input type="checkbox" class="navbar__menu-btn" id="navbar__menu-btn">
        <label for="navbar__menu-btn" class="navbar__menu-icon"><span class="navbar__nav-icon"></span></label>
        <div class="navbar__links">
          <a class="navbar__link" href="{{ url(lang + '/features.html') }}">{{ _('Features') }}</a>
          <a class="navbar__link" href="{{ url(lang + '/plugins.html') }}">{{ _('Plugins') }}</a>
          <a class="navbar__link" href="{{ url(lang + '/learn.html') }}">{{ _('Learn') }}</a>
          <a class="navbar__link" href="{{ url(lang + '/community.html') }}">{{ _('Get Involved') }}</a>
          <a class="navbar__link ml-auto navbar__btn btn--primary" href="{{ url(lang + '/download.html') }}">{{ _('Download') }}</a>
            <a class="navbar__link navbar__btn" href="#langmodal">{{ lang_full[0] }} {{ lang_full[1] }}</a>
        </div>
    </div>
</header>


<div class="modal" id="langmodal">
    <div class="modal__dialog">
        <div class="modal__header">
            <h4 class="modal__title">Select Language</h4>
            <a href="#" class="modal__close-btn">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-x"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
            </a>
        </div>
        <div class="modal__list">
            {% for key in langs_full.keys() %}
              <a class="modal__list-item" href="{{ self_localized(key) }}">{{ langs_full[key][0] }} {{ langs_full[key][1] }}</a>
            {% endfor %}
        </div>
    </div>
</div>

<div class="navbar__placeholder"></div>
