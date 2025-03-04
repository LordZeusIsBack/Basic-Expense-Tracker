from django.shortcuts import render, redirect
from django.utils import timezone
from .models import TrackingHistory, CurrentBalance
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required(login_url='login')
def index(r):
    if r.method == 'POST':
        title = r.POST.get('title')
        amount = r.POST.get('amount')
        expense_type = 'Credit'
        category = r.POST.get('category')
        date_time = r.POST.get('date_time') or timezone.now()
        current_bal, _ = CurrentBalance.objects.get_or_create(id = 1)
        if current_bal.cur_bal + int(amount) < 0:
            messages.info(r, 'Insufficient balance')
            return redirect('/')
        if int(amount) < 0: expense_type = 'Debit'
        try:
            current_bal.cur_bal += int(amount)
            current_bal.save()
            TrackingHistory.objects.create(
                current_balance = current_bal,
                title=title,
                amt=amount,
                expense_type = expense_type,
                category=category,
                created_at=date_time
            )
            return redirect('/')
        except ValueError as e:
            messages.info(r, str(e))
            return redirect('/')
    transactions= TrackingHistory.objects.all().order_by('-created_at')
    total_balance, _ = CurrentBalance.objects.get_or_create(id=1)
    credited = sum(obj.amt for obj in transactions if obj.expense_type == 'Credit')
    debited = sum(obj.amt for obj in transactions if obj.expense_type == 'Debit')
    return render(r, 'index.html', context={'expenses': transactions, 'total_balance': total_balance.cur_bal, 'total_credits': credited, 'total_debits': debited})

def delete_transaction(r, id_of_transaction):
    transaction = TrackingHistory.objects.get(id=id_of_transaction)
    current_bal = CurrentBalance.objects.get(id=1)
    current_bal.cur_bal -= transaction.amt
    current_bal.save()
    transaction.delete()
    return redirect('/')

def login_view(r):
    return render(r, 'login.html')

def register_view(r):
    return render(r, 'registration.html')

def logout_view(r):
    logout(r)
    messages.success(r, 'You have been logged out')
    return redirect('login')