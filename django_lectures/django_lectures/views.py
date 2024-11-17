from django.shortcuts import render
from django.http import HttpResponse


# views handling the requests coming from routes
def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("about page")

def contact(request):
    return HttpResponse("contact page")
