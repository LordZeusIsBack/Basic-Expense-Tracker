from django.db import models

# Create your models here.
class TrackingHistory(models.Model):
    current_balance = models.ForeignKey('CurrentBalance', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    expense_type = models.CharField(max_length=6, choices=[
        ('Credit', 'Credit'),
        ('Debit', 'Debit')
    ])
    amt = models.IntegerField()
    category = models.CharField(max_length=50, choices=[
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Utilities', 'Utilities'),
        ('Rent', 'Rent'),
        ('Entertainment', 'Entertainment'),
        ('Miscellaneous', 'Miscellaneous')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

class CurrentBalance(models.Model):
    cur_bal = models.IntegerField(default=0)
