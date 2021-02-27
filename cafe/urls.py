from django.urls import path

from . import views

urlpatterns = [
    #   path("", views.CafeList.as_view({"get": "list"}), name="cafe"),
    path("", views.CafeList.as_view(), name="cafe"),
    # path("cafe/", include("cafe.urls")),
]
