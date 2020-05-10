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
<footer>
  <div class="container footer_container">
    <div class="row">
      <div class="col-sm-8">
        <p>
        Copyright &copy; 2019-2020 The Zrythm contributors ~
        <a href="{{ url(lang + '/legal.html') }}">Legal</a>
        </p>
      </div>
      <div class="col-sm-4">
        <right>
          <a href="https://paypal.me/zrythm">
            <img
               class="footer_btn"
               alt="Donate using PayPal"
               src="{{ url('dist/fork-awesome/paypal.svg') }}">
          </a>
          <a href="https://liberapay.com/Zrythm">
            <img
               class="footer_btn"
               alt="Donate using Liberapay"
               src="{{ url('dist/fork-awesome/liberapay.svg') }}">
          </a>
          <a href="https://twitter.com/zrythmdaw">
            <img
               class="footer_btn"
               alt="Zrythm on Twitter"
               src="{{ url('dist/fork-awesome/twitter.svg') }}">
          </a>
          <a rel="me" href="https://mastodon.social/@zrythm">
            <img
               class="footer_btn"
               alt="Zrythm on Mastodon"
               src="{{ url('dist/fork-awesome/mastodon.svg') }}">
          </a>
        </right>
      </div>
    </div>
</footer>
