from django.shortcuts import render

from rest_framework import viewsets, filters
from rest_framework.response import Response

from .models import Lead
from .serializers import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    
    def perform_create(self, serializer):

        serializer.save(created_by=self.request.user)