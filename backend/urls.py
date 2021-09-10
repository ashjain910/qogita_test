"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework import routers

from django.contrib import admin

from django.urls import path, include
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


from app import views
from rest_framework.schemas import get_schema_view


dr_router = routers.DefaultRouter(trailing_slash=True)

dr_router.register(r"address", views.AddressView, basename="address")

from rest_framework import permissions


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    url("^", include(dr_router.urls)),
]