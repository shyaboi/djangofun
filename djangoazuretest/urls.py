from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('weather/', include('weather.urls')),
    path('admin/', admin.site.urls),
]