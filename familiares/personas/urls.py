from django.urls import path

from personas.views import personas

urlpatterns =[
    path('', personas, name = 'personas'),
]