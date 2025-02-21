from django.shortcuts import render, redirect
from django.utils import timezone
from .models import TrackingHistory, CurrentBalance

# Create your views here.
def index(r):
    if r.method == 'POST':
        title = r.POST.get('title')
        amount = r.POST.get('amount')
        expense_type = 'Credit'
        category = r.POST.get('category')
        date_time = r.POST.get('date_time') or timezone.now()
        current_bal, _ = CurrentBalance.objects.get_or_create(id = 1)
        if int(amount) < 0: expense_type = 'Debit'
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
    return render(r, 'index.html')