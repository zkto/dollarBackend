from django.shortcuts import render
from rest_framework import viewsets
from dollar.serializers import DollarClpSerializer
from dollar.models import DollarClp
import rest_framework_filters as filters
# from django_filters import FilterSet, DateFromToRangeFilter


class DateFilter(filters.FilterSet):

    class Meta:
        model = DollarClp
        fields = {
            'date': ['lte', 'gte', 'range'],
            'price': ['lte', 'gte', 'range']
        }


class DollarViewSet(viewsets.ModelViewSet):
    filter_class = DateFilter
    queryset = DollarClp.objects.all()
    serializer_class = DollarClpSerializer




