from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from portfolio import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
