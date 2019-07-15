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
