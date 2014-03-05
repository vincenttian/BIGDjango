from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Avg
from website.fund_tracker.models import Stock

from django.contrib import messages

import urllib


def __request(symbol, stat):
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, stat)
    return urllib.urlopen(url).read().strip().strip('"')

def get_price(symbol): 
    return __request(symbol, 'l1')

def get_price_earnings_growth_ratio(symbol): 
    return __request(symbol, 'r5')

def get_price_book_ratio(symbol): 
    return __request(symbol, 'p6')

def get_volume(symbol): 
    return __request(symbol, 'v')

def get_stock_exchange(symbol): 
    return __request(symbol, 'x')

class StockListView(ListView):
    template_name = 'stock_list.html'
    model = Stock

    def get_context_data(self, **kwargs):
        context = super(StockListView, self).get_context_data(**kwargs)
        for stock in context['stock_list']:
        	stock.exchange = get_stock_exchange(stock.symbol)
        	stock.current_price = get_price(stock.symbol)
        	stock.current_PE = get_price_earnings_growth_ratio(stock.symbol)
        	stock.current_PB = get_price_earnings_growth_ratio(stock.symbol)
        	stock.volume = get_volume(stock.symbol)
        return context