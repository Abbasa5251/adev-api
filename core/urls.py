from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
]


admin.site.site_header = "ADev Portfolio API Admin"
admin.site.site_title = "ADev API Admin Portal"
admin.site.index_title = "Welcome to ADev API Portal"
