from rest_framework import serializers

from main.models import Declaration


class DeclarationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Declaration
        fields = '__all__'
