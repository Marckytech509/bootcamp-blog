from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include('bcmp.urls')),
    url(r'^$', views.page),
]

admin.site.site_header = "Administration au Bootcamp project"
admin.site.site_title = "Bootcamp project"
admin.site.index_title = "Bienvenue Admin"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
