from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cafe/", include("cafe.urls")),
    path("member/", include("member.urls")),
]
