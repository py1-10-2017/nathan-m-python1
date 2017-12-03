# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
	if request.session:
		return render(request, 'ecommerce/index.html')
	else:
		request.session['item_count'] = 0
		request.session['grand_total'] = 0	
		return render(request, 'ecommerce/index.html')

def total(request):
	product_costs = {
		'a100': 4.99,
		'a200': 5.99,
		'a300': 6.99,
		'a400': 7.99 		
	}

	quantity = float(request.POST['quantity'])
	product_id = request.POST['product_id']
	cost = product_costs[product_id]
	request.session['total'] = cost * quantity

	request.session['item_count'] = request.session.get('item_count', 0) + int(quantity)
	request.session['grand_total'] = request.session.get('grand_total', 0) + request.session['total']
	return redirect('/checkout')

def checkout(request):
	return render(request, 'ecommerce/checkout.html')

def clear_sessions(request):
	request.session['item_count'] = 0
	request.session['grand_total'] = 0
	return render(request, 'ecommerce/index.html')	

