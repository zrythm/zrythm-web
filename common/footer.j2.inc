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
    <a href="https://u.fsf.org/16e"><img height="86" src="{{ url('static/images/fsfs_icons_red-bg.png') }}" alt="Free Software. Free Society."></a>
    <a href="http://endsoftpatents.org/"><img width="180" src="{{ url('static/images/esp-logo-horizontal.png') }}" alt="End Software Patents"></a>
    <a href="https://www.gnu.org/philosophy/javascript-trap.html"><img width="120" src="{{ url('static/images/freejs.png') }}" alt="FreeJS"></a>
    <a href="https://www.fsf.org/campaigns/playogg/en/"><img width="120" src="{{ url('static/images/Ogg_button_final.png') }}" alt="Play OGG"></a>
    <p style="padding-bottom: 12px;"></p>
  </div>
</footer>
