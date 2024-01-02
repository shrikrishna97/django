from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaulttags import register

@register.filter
def get_range(value):
    return list(range(1, int(value)+1))

def home(request):
    return render(request,"index.html", {"year":2024, "day": "somvar"})
    # return HttpResponse("<h2>new years bolte</h2>")

def genrate(request):
    num = request.GET.get("num")
    upto = request.GET.get("upto")
    return render(request, "show_table.html",{"num": num, "upto": upto})