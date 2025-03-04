from django.db import models
from django.conf import settings

# Create your models here.
class TrackingHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.amt == '0': raise ValueError('0 is not a valid transaction')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.title} ({self.expense_type}): {self.amt}"

class CurrentBalance(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cur_bal = models.IntegerField(default=0)

    def __str__(self):
        return f'Current balance: {self.user.username} - Balance: {self.cur_bal}'
