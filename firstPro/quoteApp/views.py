from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def displayQuote(request):
    return HttpResponse("best investment is me")
