from django.contrib import admin
from django.urls import path, include
from . import settings

urlpatterns = [
    # Paths del core
    path('', include('core.urls')),
    # Paths del service
    path('services/', include('services.urls')),
    # Paths del blog
    path('blog/', include('blog.urls')),
    # Paths del pages
    path('page/', include('pages.urls')),
    # Paths del admin
    path('admin/', admin.site.urls),
]

# Si estamos en debug=true, ¿Qué hacer con las imgs?
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)