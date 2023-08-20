from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/projects/", include("project.urls")),
    path("api/v1/contact/", include("contact.urls")),
    path("api/v1/skills/", include("skill.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "ADev Portfolio API Admin"
admin.site.site_title = "ADev API Admin Portal"
admin.site.index_title = "Welcome to ADev API Portal"
