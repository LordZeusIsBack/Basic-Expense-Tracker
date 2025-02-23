from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.safestring import mark_safe
from .models import TrackingHistory, CurrentBalance
from django.contrib import messages
from pandas import DataFrame

# Create your views here.
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
    transactions= TrackingHistory.objects.all().order_by('-created_at')
    if transactions:
        df = DataFrame(list(transactions.values()))
        df.rename(columns={
            'title': 'Title',
            'amt': 'Amount',
            'category': 'Category',
            'created_at': 'Created At'
        }, inplace=True)
        html_table = df.to_html(index=False, classes='table table-bordered', columns=['Title', 'Amount', 'Category', 'Created At'])
    else: html_table = '<p>No transactions yet</p>'
    safe_html_table = mark_safe(html_table)
    total_balance, _ = CurrentBalance.objects.get_or_create(id=1)
    credited = sum(obj.amt for obj in transactions if obj.expense_type == 'Credit')
    debited = sum(obj.amt for obj in transactions if obj.expense_type == 'Debit')
    return render(r, 'index.html', context={'total_balance': total_balance.cur_bal, 'table_html': safe_html_table, 'total_credits': credited, 'total_debits': debited})