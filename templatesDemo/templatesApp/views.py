from django.shortcuts import render

def renderTemplates(request):
    my_dict={"name": "Bharath"}
    return render(request, 'templatesApp/firstTemplates.html', context=my_dict)

def renderEmployee(request):
    my_dict={"id": 123, "name": "Johb", "sal": 10000}
    return render(request, 'templatesApp/employeeTemplates.html',my_dict)    
# Create your views here.
