from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def h_test(text):
    return HttpResponse("<h1>" + str(text) + "</h1>")


def home(request):
    return render(request,'')


def services(request):
    return h_test('Our Services')
