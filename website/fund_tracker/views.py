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

class StockListView(ListView):
    template_name = 'stock_list.html'
    model = Stock

    def get_context_data(self, **kwargs):
        context = super(StockListView, self).get_context_data(**kwargs)
        return context