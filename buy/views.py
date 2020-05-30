from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Buy

def landing(request):
    return render(request, 'buy/home.html', context={})

class ShopView(ListView):
    model = Buy
    template_name = 'buy/shop.html'
    context_object_name = 'buys'

    def get_queryset(self):
        result = super(ShopView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Buy.objects.filter(title__contains=query)
            result = postresult
        else:
            result = None
        return result
