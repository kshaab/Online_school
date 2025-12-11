from django.contrib import admin
from django.templatetags.static import static
from django.urls import path, include

from online_school import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("courses/", include("lms.urls", namespace="lms")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)