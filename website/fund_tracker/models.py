from django.db import models
# Create your models here.

class Stock(models.Model):
	symbol = models.CharField(max_length=10)
	exchange = models.CharField(max_length=10)
	shares = models.IntegerField()
	entering_price = models.IntegerField()

	def __unicode__(self):
		return str(self.shares) + " shares of the company " + self.company_name + " was bought as " + self.symbol + \
				" on " + self.exchange + " at " + str(self.entering_price) + " dollars."

"""
Implement in the future
class Fund(models.Model):
	name = models.CharField(Max_length=100)
	stocks = models.ManyToManyField(Stock)
	total_value_under_management = models.IntegerField()

	def __unicode__(self):
		return "The " + self.name + " has " + str(total_value_under_management) + " dollars under management."
"""