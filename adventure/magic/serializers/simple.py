from rest_framework import serializers

from adventure.magic.models import Card, Print, Set


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


class PrintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Print
        fields = '__all__'


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = '__all__'
