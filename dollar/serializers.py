from rest_framework import serializers
from dollar.models import DollarClp


class DollarClpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DollarClp
        fields = ('price', 'date', 'price_difference', 'date_update', 'week_value')

