from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template


def show(request):
    t = get_template('technology/technology.html')
    html = t.render(Context({}))
    return HttpResponse(html)


