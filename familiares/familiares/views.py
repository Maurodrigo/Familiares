from django.http import HttpResponse
from django.shortcuts import render

def familiar(request):
    return render(request, 'familiares.html')