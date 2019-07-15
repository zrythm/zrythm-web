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
<footer id="footer">
  <div class="container-fluid cushion-below text-center">
    <div class="container">
      <div class="row">
        <div class="col-12 col-sm-4">
          <ul class="footer-list">
            <li><p><a href="team.html">{{ _("Team") }}</a></p></li>
            <li><p><a href="contact.html">{{ _("Contact") }}</a></p></li>
            <li><p><a href="about.html">{{ _("About Zrythm") }}</a></p></li>
          </ul>
        </div>
        <div class="col-12 col-sm-4">
          <ul class="footer-list">
            <li><p><a href="{{ issue_tracker }}">{{ _("Issue Tracker") }}</a></p></li>
            <li><p><a href="{{ git_url }}">{{ _("Source Code") }}</a></p></li>
            <li><p><a href="javascript.html" rel="jslicense">{{ _("JavaScript Licenses") }}</a></p></li>
          </ul>
        </div>
        <div class="col-12 col-sm-4">
          <ul class="footer-list">
            <li><p><a href="https://manual.zrythm.org/{{ lang }}">{{ _("Manual") }}</a></p></li>
            <li><p><a href="faq.html">{{ _("FAQ") }}</a></p></li>
            <li><p><a href="join-us.html">{{ _("Support Us") }}</a></p></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="container text-center">
    <p>
    {% trans %}
    Copyright &copy; 2019 Alexandros Theodotou et al.<br>
    <a href="{{ git_web_url }}">Source code of this site.</a></br>
    Report issues with this website to <a href="https://savannah.nongnu.org/support/?func=additem&group=zrythm">us</a>.
    {% endtrans %}
    </p>
    <p style="padding-bottom: 12px;"></p>
  </div>
</footer>
