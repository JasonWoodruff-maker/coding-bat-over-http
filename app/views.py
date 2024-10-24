from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
from django.http import HttpResponse


def nearhundred(request, x: int):
    if 90 <= x <= 110:
        return HttpResponse(True)
    elif 190 <= x <= 210:
        return HttpResponse(True)
    else:
        return HttpResponse(False)
