from rest_framework import serializers


class MetricSerializer(serializers.Serializer):
    query = serializers.CharField(max_length=1000)
