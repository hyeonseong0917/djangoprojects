from django.shortcuts import render

def renderTemplates(request):
    return render(request, 'templatesApp/firstTemplates.html')
# Create your views here.
