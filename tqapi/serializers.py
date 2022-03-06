from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from tqapi.models import Docuware


class TqApiSerializer(serializers.ModelSerializer):
    "Serializer data coming from tq model api"
    class Meta:
        model = Docuware
        fields = "__all__"
