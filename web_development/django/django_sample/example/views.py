from django.http import HttpResponse
from django.shortcuts import render


def view_sample_page(request):
    return HttpResponse("Welcome to the sample page!")
