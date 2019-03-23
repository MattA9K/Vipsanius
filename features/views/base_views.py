# Author - Matt Andrzejczuk


from django.http import HttpResponse
from django.template import loader




def home_page(request):
    template = loader.get_template("index.html")
    visitor = request.META
    context = {"visitor": visitor}
    return HttpResponse(template.render(context))
