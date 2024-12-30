from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
# from rest_framework.decorators import api_view

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def perform_create(self, serializer):
        client_id = self.request.data.get('client')
        client = Client.objects.get(id=client_id)
        serializer.save(client=client)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @action(detail=True, methods=['get'])
    def loans(self, request, pk=None):
        client = self.get_object()  # Get the client instance
        loans = Loan.objects.filter(client=client)
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)

class GuarantorViewSet(viewsets.ModelViewSet):
    queryset = Guarantor.objects.all()
    serializer_class = GuarantorSerializer

    def perform_create(self, serializer):
        loan_id = self.request.data.get('loan')
        loan = Loan.objects.get(id=loan_id)
        serializer.save(loan=loan)

