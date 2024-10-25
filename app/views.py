from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
from django.http import HttpResponse


def near_hundred(request, x: int):
    if 90 <= x <= 110:
        return HttpResponse(True)
    elif 190 <= x <= 210:
        return HttpResponse(True)
    else:
        return HttpResponse(False)


def string_splosion(request, word):
    result = ""
    for i in range(0, len(word) + 1, 1):
        result = result + word[0:i]
    return HttpResponse(result)
def cat_dog(request, dog):
    if dog.count("cat") == dog.count("dog"):
        return HttpResponse(True)
    else:
        return HttpResponse(False)
    
def logic_2(request, a, b, c):
    inputs = [a,b,c]

    total = 0

    for x in inputs:
        if inputs.count(x) == 1:
            total += int(x)

    return HttpResponse(total)


