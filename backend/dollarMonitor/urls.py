"""dollarMonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from dollar.models import DollarClp
from rest_framework import routers, serializers, viewsets


"""
# Serializers define the API representation.
class DollarClpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DollarClp
        fields = ('price', 'date', 'price_difference', 'date_update', 'week_value')


# ViewSets define the view behavior.
class DollarViewSet(viewsets.ModelViewSet):
    queryset = DollarClp.objects.all()
    serializer_class = DollarClpSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'dollars', DollarViewSet)

"""

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^', include(router.urls)),
    url(r'^', include('dollar.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
