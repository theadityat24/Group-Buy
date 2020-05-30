from django.shortcuts import render

def landing(request):
    return render(request, 'buy/home.html', context={})