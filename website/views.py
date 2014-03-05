from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render

def home(request):     
	return render(request, 'index.html')

def about(request):     
	return render(request, 'about.html')

def news(request):     
	return render(request, 'news.html')

def team(request):     
	return render(request, 'team.html')

def fund(request):     
	return render(request, 'fund.html')

def resources(request):     
	return render(request, 'resources.html')

def join(request):     
	return render(request, 'join.html')
