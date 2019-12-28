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

<header>
  <a href="index.html" class="logo">
    <img class="logo_img" width=28
       src="{{ url('static/images/z-xmas.png') }}"
       alt="Logo">
    </img>
  </a>
  <a href="index.html" class="button">
    {% trans %}
    Home
    {% endtrans %}
  </a>
  <a href="download.html" class="button">
    {% trans %}
    Download
    {% endtrans %}
  </a>
  <a href="reference.html" class="button">
    {% trans %}
    Reference
    {% endtrans %}
  </a>
  <a href="community.html" class="button">
    {% trans %}
    Community
    {% endtrans %}
  </a>
  <label for="modal-control"
     class="button globe">
    <img class="logo_img" width=28
       src="{{ url('static/icons/breeze/globe.svg') }}"
       alt="Logo">
    </img>
  </label>
</header>

<input type="checkbox" id="modal-control" class="modal">
<div>
  <div class="card">
    <label for="modal-control" class="modal-close"></label>
    <h3 class="section">
      {% trans %}
      Language
      {% endtrans %}
    </h3>
    <p class="section">
      {% for key in langs_full.keys() %}
        <a href="{{ self_localized(key) }}">
          {{ langs_full[key] }}
        </a>
      {% endfor %}
    </p>
  </div>
</div>
