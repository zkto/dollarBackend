from django.urls import include, path
from rest_framework import routers
from dollar import views
from django.urls import path, include
from django.conf.urls import url


router = routers.DefaultRouter()
router.register(r'dollars', views.DollarViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]