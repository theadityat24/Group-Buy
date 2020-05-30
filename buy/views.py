from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
    contributions = Contribution.objects.filter(buy=buy).count()

    return render(request, 'buy/shopdetail.html', context={'buy': buy, 'contributions': contributions})

@login_required
def checkout(request):
    if request.method == 'POST':
        p = request.POST
        p['user'] = request.user
        p['buy'] = Buy.objects.get(request.GET.get('id'))
        form = ContributionCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form = ContributionCreationForm()

    return render(request, 'buy/checkout.html', context={
        'form': form,
        'buy': Buy.objects.get(request.GET.get('id')), 
    })

def shop_search(request):
    return render(request, 'buy/shop_search.html', context={
        'buys': Buy.objects.filter(title__contains=request.GET.get('query'))[:8]
    })


    

    