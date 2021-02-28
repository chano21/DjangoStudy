from django.urls import path

from . import views

urlpatterns = [
    path("list", views.MemberList.as_view(), name="memberlist"),
    path("", views.MemberOne.as_view(), name="member"),
]
