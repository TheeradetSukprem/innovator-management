from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/projects/", include("projects.urls")),
    path("api/skills/", include("skills.urls")),
    path("api/users/", include("users.urls")),
]
