from django.contrib import admin
from django.urls import include, path, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .initialize import settings


schema_view = get_schema_view(
    openapi.Info(
        title="Swagger Title",
        default_version="1",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(name="test", email="your@test.com"),
    ),
    public=True,
)
swaggers = [
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

urls = [
    path("admin/", admin.site.urls),
    path("cafe/", include("cafe.urls")),
    path("member/", include("member.urls")),
]
urlpatterns = []

# debug 모드일때 swagger 허용
if settings.DEBUG:
    urlpatterns = urls + swaggers
else:
    urlpatterns = urls
