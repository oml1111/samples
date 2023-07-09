from django.http import HttpResponse
from django.shortcuts import render


def view_sample_page(request):
    return HttpResponse("Welcome to the sample page!")


def view_template_sample(request):
    str_var = "Hello World!"
    return render(request, "sample.html", {'str_variable': str_var})

