from django.urls import path, include

urlpatterns = [
    path("", include("tasks.urls")),
    path("api-auth/", include("rest_framework.urls")),
]