{% for n in news %}
<article>
<h3 style="margin-bottom: 0px">
  <a href="{{ n['link'] }}">
    {{ n['title'] }}
  </a>
</h3>
<small><i><h6>
  {{ _('posted by') + ' ' + n['author'] + ' ' + _('on') + ' ' + datetime_parse(n['updated']).strftime('%Y-%m-%d') }}
</h6></i></small>
{{ truncatehtml(n['content'][0]['value'], 680, '<a style="text-decoration: none" href=\"' + n['link'] + '\">...</a>').replace('<h3>','<h4>').replace('<br></br>','<br>') }}
</article>
{% endfor %}
<!--{% include "news/2019-06-19-mailing-lists-up.j2.inc" %}
{% include "news/2019-06-07-zrythm-translations-hosted-weblate-org.j2.inc" %}
{% include "news/2019-05-04-translation-portal-launched.j2.inc" %} -->
<a href="https://savannah.nongnu.org/news/?group=zrythm"><h3>{{ _("More news")}}</h3></a>
