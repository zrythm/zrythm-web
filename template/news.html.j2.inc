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
