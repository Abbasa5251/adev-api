from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

schema_view = get_schema_view(
    openapi.Info(
        title="ADev Tutorials",
        default_version="v1",
        description="API for ADev Tutorials",
        contact=openapi.Contact(email="adevtuts@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/projects/", include("project.urls")),
    path("api/v1/contact/", include("contact.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "ADev Portfolio API Admin"
admin.site.site_title = "ADev API Admin Portal"
admin.site.index_title = "Welcome to ADev API Portal"
