
from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit
def home(request, *args,**kwargs):
    querySet=PageVisit.objects.filter(path=request.path)
    total_query=PageVisit.objects.all()
    template_name="home.html"
    my_context={
        "page_title":"my page",
        "total_visit":total_query,
        "queryset":querySet.count(),
    }
    path=request.path
    print()
    PageVisit.objects.create()
    return  render(request,template_name,my_context)
