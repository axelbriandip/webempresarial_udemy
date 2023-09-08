from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Paths del core
    path('', include('core.urls')),

    # Paths del admin
    path('admin/', admin.site.urls),
]