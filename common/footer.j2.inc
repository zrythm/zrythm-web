<footer id="footer">
  <div class="container-fluid cushion-below">
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
            <li><p><a href="{{ git_url }}/issues">{{ _("Issue Tracker") }}</a></p></li>
            <li><p><a href="{{ git_url }}">{{ _("Source Code") }}</a></p></li>
            <li><p><a href="javascript.html" rel="jslicense">{{ _("JavaScript Licenses") }}</a></p></li>
          </ul>
        </div>
        <div class="col-12 col-sm-4">
          <ul class="footer-list">
            <li><p><a href="https://manual.zrythm.org">{{ _("Manual") }}</a></p></li>
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
    <a href="https://git.zrythm.org/zrythm/zrythm-web">Source code of this site.</a></br>
    Report issues with this website to <a href="https://git.zrythm.org/zrythm/zrythm-web/issues">us</a>.
    {% endtrans %}
    </p>
    <a href="https://u.fsf.org/16e"><img height="86" src="{{ url('static/images/fsfs_icons_red-bg.png') }}" alt="Free Software, Free Society"></a>
    <a href="https://creativecommons.org/"><img style="fill: red;" height="48" src="{{ url('static/images/cc_logo.svg') }}" alt="Creative Commons"></a>
    <p></p>
  </div>
</footer>
