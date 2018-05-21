
from django.shortcuts import render


def index_page(request):
    render(request, "index.html", context={})
