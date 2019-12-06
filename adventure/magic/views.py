"""Views for the magic app"""
from rest_framework import generics

from .models import (
    Card,
    Print,
    Set,
)
from .serializers.simple import CardSerializer, PrintSerializer, SetSerializer


class CardView(generics.ListAPIView):
    """Card view"""
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class PrintView(generics.ListAPIView):
    """Print view"""
    queryset = Print.objects.all()
    serializer_class = PrintSerializer


class SetView(generics.ListAPIView):
    """Set view"""
    queryset = Set.objects.all()
    serializer_class = SetSerializer
