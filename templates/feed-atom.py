import jinja2

env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
print(env.get_template("feed.rss.j2").render(items=get_list_of_items()))
