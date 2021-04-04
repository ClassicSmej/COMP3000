from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('accounts.urls')),
    path('home/', include('home.urls')),
    path('device/', include('device.urls')),
    path('help/', include('help.urls')),
]
