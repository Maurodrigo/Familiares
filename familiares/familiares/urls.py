from django.contrib import admin
from django.urls import path, include
from familiares.views import familiar

urlpatterns = [
    path('familia/', include('personas.urls')),
    path('admin/', admin.site.urls),
]
