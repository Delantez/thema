from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)

class Client(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    sur_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    tribe = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    residence = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    home_address = models.CharField(max_length=255)
    chair_person = models.CharField(max_length=255)
    spouse_name = models.CharField(max_length=255, blank=True, null=True)
    spouse_phone = models.CharField(max_length=20, blank=True, null=True)
    work_place = models.CharField(max_length=255)
    work = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    employee = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.sur_name}"
    
class Loan(models.Model):
    client = models.ForeignKey(Client, related_name='loans', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    bank = models.CharField(max_length=255)
    branch = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(max_length=255)
    amount_in_bank = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    guarantee = models.CharField(max_length=255)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    altGuarantee = models.CharField(max_length=255)
    altAttachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Loan for {self.client.first_name} {self.client.second_name} {self.client.sur_name}- Amount: {self.amount}"

    def clean(self):
        if self.amount <=0:
            raise ValidationError('loan must be positive')
        if self.duration <=0:
            raise ValidationError('Duration must be positive')
        
class Guarantor(models.Model):
    client = models.ForeignKey(Client, related_name='guarantors', on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, related_name='guarantors', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    sur_name = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    residence = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    spouse_name = models.CharField(max_length=255, blank=True, null=True)
    spouse_phone = models.CharField(max_length=20, blank=True, null=True)
    work_place = models.CharField(max_length=255)
    work = models.CharField(max_length=255)
    income = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Guarantor: {self.first_name} {self.sur_name} for Client: {self.client.first_name} {self.client.sur_name}- Loan: {self.loan.amount}"
    
    

class Rejesho(models.Model):
    loan = models.ForeignKey(Loan, related_name='rejesho', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    rejesho = models.DecimalField(max_digits=10, decimal_places=2)  # Amount paid back
    riba = models.DecimalField(max_digits=10, decimal_places=2)  # Interest amount
    staff = models.CharField(max_length=255)  # Staff handling the transaction
    jumla = models.DecimalField(max_digits=10, decimal_places=2)  # Total payment (rejesho + riba)

    def __str__(self):
        return f"Rejesho {self.id} for Loan {self.loan.id}"