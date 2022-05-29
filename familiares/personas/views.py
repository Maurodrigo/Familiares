from django.shortcuts import render
from personas.models import Personas

# Create your views here.
def personas(request):
        personas = Personas.objects.all()
        context = {'personas':personas}
        return render(request, 'familiares.html', context=context)