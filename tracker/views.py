from django.shortcuts import render, redirect
from django.utils import timezone
from .models import TrackingHistory, CurrentBalance
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth import get_user_model

# Create your views here.
@login_required(login_url='login')
def index(r):
    if r.method == 'POST':
        title = r.POST.get('title')
        amount = r.POST.get('amount')
        expense_type = 'Credit'
        category = r.POST.get('category')
        date_time = r.POST.get('date_time') or timezone.now()
        print(r.user)
        current_bal, _ = CurrentBalance.objects.get_or_create(user=r.user)
        if current_bal.cur_bal + int(amount) < 0:
            messages.info(r, 'Insufficient balance')
            return redirect('/')
        if int(amount) < 0: expense_type = 'Debit'
        try:
            current_bal.cur_bal += int(amount)
            current_bal.save()
            TrackingHistory.objects.create(
                user=r.user,
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
    transactions= TrackingHistory.objects.filter(user=r.user).order_by('-created_at')
    total_balance, _ = CurrentBalance.objects.get_or_create(user=r.user)
    credited = sum(obj.amt for obj in transactions if obj.expense_type == 'Credit')
    debited = sum(obj.amt for obj in transactions if obj.expense_type == 'Debit')
    return render(r, 'index.html', context={'expenses': transactions, 'total_balance': total_balance.cur_bal, 'total_credits': credited, 'total_debits': debited})

@login_required(login_url='login')
def delete_transaction(r, id_of_transaction):
    transaction = TrackingHistory.objects.get(id=id_of_transaction, user=r.user)
    current_bal = CurrentBalance.objects.get(id=transaction.current_balance.id, user=r.user)
    current_bal.cur_bal -= transaction.amt
    current_bal.save()
    transaction.delete()
    return redirect('/')

def login_view(r):
    if r.method == 'POST':
        login_input = r.POST.get('username')
        password = r.POST.get('password')
        user = authenticate(username=login_input, password=password)
        if user:
            login(r, user)
            messages.success(r, 'You have been logged in')
            return redirect('/')
        messages.error(r, 'Invalid credentials')
        return redirect('login')
    return render(r, 'login.html')

def register_view(r):
    if r.method == 'POST':
        User = get_user_model()
        user_name = r.POST.get('username')
        email = r.POST.get('email')
        password1 = r.POST.get('password2')
        password2 = r.POST.get('password2')
        if User.objects.filter(username=user_name).exists():
            messages.info(r, 'Username already exists')
            return redirect('registration')
        if password1 != password2:
            messages.error(r, 'Passwords do not match')
            return redirect('registration')
        user = User.objects.create_user(username=user_name, email=email, password=password1)
        user.save()
        messages.success(r, 'Account created successfully')
        return redirect('login')
    return render(r, 'registration.html')

def logout_view(r):
    logout(r)
    messages.success(r, 'You have been logged out')
    return redirect('login')
