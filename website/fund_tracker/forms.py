from django import forms
from django.forms.models import modelformset_factory
from website.fund_tracker.models import Stock

class StockForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(StocokForm, self).__init__(*args, **kwargs)
	class Meta:
		model = Stock
