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
<a href="https://savannah.nongnu.org/news/?group=zrythm"><h3>{{ _("More news")}}</h3></a>
