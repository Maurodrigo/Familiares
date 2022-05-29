from django.contrib import admin
from django.urls import path
from familiares.views import familiar

urlpatterns = [
    path('familia/', familiar, name = 'familiar'),
    path('admin/', admin.site.urls),
]
