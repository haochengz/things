
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect, reverse

items = []

class IndexView(View):

    @staticmethod
    def get(request):
        return render(request, "index.html", {
            "list": items
        })

    @staticmethod
    def post(request):
        item = request.POST.get('new_item', '')
        items.append(item)
        return redirect(reverse("index"))

