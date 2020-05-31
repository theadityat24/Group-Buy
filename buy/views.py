from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage


import smtplib

from .models import Buy, Contribution
from .forms import ContributionCreationForm

def landing(request):
    return render(request, 'buy/home.html', context={})


def shop_view(request):
    buys = Buy.objects.order_by('-date_started')[:8]
    context = {
        'top1': buys[:4],
        'top2': buys[4:]
    }
    return render(request, 'buy/shop.html', context=context)

def shop_detail(request, id):
    buy = Buy.objects.get(id=id)
    contributions = Contribution.objects.count()

    return render(request, 'buy/shopdetail.html', context={'buy': buy, 'contributions': contributions})

@login_required
def checkout(request, id):
    buy = Buy.objects.get(id=id)
    if request.method == 'POST':
        p = dict(request.POST)
        p['user'] = request.user
        p['buy'] = buy
        form = ContributionCreationForm(p)
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form = ContributionCreationForm()
    
    return render(request, 'buy/checkout.html', context={
        'form': form,
        'buy': buy, 
        'shipping': int(buy.price) * .1,
        'total': int(buy.price) * 1.1,
    })

def shop_search(request):
    return render(request, 'buy/shop_search.html', context={
        'buys': Buy.objects.filter(title__contains=request.GET.get('query'))[:8]
    })

def thanks(request):

        # Sending emails without attachments using Python.
    # importing the required library. 
    
    # creates SMTP session 
    email = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # TLS for security 
    email.starttls() 
    
    # authentication
    # compiler gives an error for wrong credential. 
    email.login("grate.ecommerce@gmail.com", "Grate!Email!Password!15") 
    
    # message to be sent 
    message = "Thank you for purchasing 1 Namiki Urushi Lacquer Fountain Pen for $1320 total, including shipping and handling."
    
    # sending the mail 
    email.sendmail("grate.ecommerce@gmail.com", 'pythontestemail123456@gmail.com', message) 
    
    # terminating the session 
    email.quit()
    return render(request, 'buy/thanks.html')


    

    