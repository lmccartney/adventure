"""Views for the magic app"""
from rest_framework import generics, serializers

from .models import (
        Card,
        Print,
        Set,
)


class CardView(generics.ListAPIView):
    """Card view"""
    queryset = Card.objects.all()

    class Serializer(serializers.Serializer):
        class Meta:
            model = Card
            fields = '__all__'

    def get_serializer(self, *args, **kwargs):
        return self.Serializer(*args, **kwargs)


class PrintView(generics.ListAPIView):
    """Print view"""
    queryset = Print.objects.all()

    class Serializer(serializers.Serializer):
        class Meta:
            model = Print
            fields = '__all__'

    def get_serializer(self, *args, **kwargs):
        return self.Serializer(*args, **kwargs)


class SetView(generics.ListAPIView):
    """Set view"""
    queryset = Set.objects.all()

    class Serializer(serializers.Serializer):
        class Meta:
            model = Set
            fields = '__all__'

    def get_serializer(self, *args, **kwargs):
        return self.Serializer(*args, **kwargs)
