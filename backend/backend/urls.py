"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# Swagger
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="RythmTechnologies",
        default_version="v1",
        description="RythmTechnologies",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="technologiesrythm@gmail.com"),
        license=openapi.License(name="Mit License", url="https://github.com/RythmSoft-Co/congenial-dollop/blob/master/license"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("blog-api/", include("apps.blog.urls")),
    path("about-api/", include("apps.about.urls")),
    path("contact-api/", include("apps.contact.urls")),
    path("projects-api/", include("apps.projects.urls")),
    path("socials-api/", include("apps.socials.urls")),
    path("links-api/", include("apps.links.urls")),
    path("subs-links-api/", include("apps.subslinks.urls")),
    path("teams-api/", include("apps.team.urls")),
    path("testimonials-api/", include("apps.testimonials.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
