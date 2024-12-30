from rest_framework import serializers
from . models import *

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class LoanSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = Loan
        fields = '__all__'
    
    def validate(self, data):
        if data['amount'] <= 0:
            raise serializers.ValidationError('Loan amount must be positive')
        if data['duration'] <= 0:
            raise serializers.ValidationError('Duration must be positive')
        return data
    
class ClientWithLoanSerializer(serializers.ModelSerializer):
    loans = LoanSerializer(many=True, read_only=True)

    class Meta:
        model =Client
        fields = ['id', 'first_name', 'second_name', 'sur_name', 'loans']

        
class GuarantorSerializer(serializers.ModelSerializer):
    loan = serializers.PrimaryKeyRelatedField(queryset=Loan.objects.all())
    
    class Meta:
        model = Guarantor
        fields = '__all__'
