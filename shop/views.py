# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Flower
from .models import Order
from .util import basket_list
from .util import flow_count_name
from .util import suma
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import UpdateView, CreateView, ListView, DeleteView
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Submit, Button
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from time import time
from .util import is_digit
from datetime import datetime







###########################################################################
def main_page(request):
	flowers = Flower.objects.all()
	fl_count = flow_count_name(request)
	count = len(basket_list(request))
	return render(request, 'shop/main.html', {'flowers':flowers, 'count': count,
   'fl_count': fl_count})


#####################################################################
def about_me(request):
	return render(request, 'shop/about.html', {})


####################################################################
def contacts(request):
	return render(request, 'shop/contacts.html', {})








####################################################################
def basket(request):
   return render(request, 'shop/basket.html',
     {'flowers':basket_list(request), 'price_list': suma(request)})







################################################################

#order_confirm


def order_confirm(request):
  if request.method == "POST":
    if request.POST.get('add_button') is not None:
      errors = {}
      data = {}
      body = request.POST.get('body', '').strip()
      data['body'] = body
      syma = suma(request)
      data['syma'] = syma
      name = request.POST.get('name', '').strip()
      if not name:
        errors['name'] = u"Ведіть імя!"
      else:
        data['name'] = name
      number = request.POST.get('number', '').strip()
      if not number:
        errors['number'] = u"Ведіть номер!"
      else:
        data['number'] = number
      
           
      if not errors:
        order = Order(**data)
        order.save()
        return HttpResponseRedirect( u'%s?status_message=Замовлення успішно сформовано!'  % reverse('main'))
      else:
        return render(request, 'shop/order_confirm.html',
        {'flowers':basket_list(request), 'price_list': suma(request),'errors': errors})
    elif request.POST.get('cancel_button') is not None:
      return HttpResponseRedirect( u'%s?status_message=Формування замовлення скасовано!' % reverse('main'))
  else:
   return render(request, 'shop/order_confirm.html',
     {'flowers':basket_list(request), 'price_list': suma(request)})







#####################################################################
def one_flower(request, pk):
  flower = Flower.objects.filter(pk=pk)
  fl_count = flow_count_name(request)
  count = len(basket_list(request))
  return render(request, 'shop/one_flower.html', {'flower':flower, 'count': count, 'fl_count': fl_count})









######################################################################
@login_required
def orders(request):
  orders = Order.objects.all()
  return render(request, 'shop/orders.html', {'orders': orders})




#########################################################################
#flower_add

def flower_add(request):
  # was form posted?
  if request.method == "POST":
    # was form add button clicked?
    if request.POST.get('add_button') is not None:
      # errors collection
      errors = {}
      # data for student object
      data = {}
      # validate user input
      title = request.POST.get('title', '').strip()
      if not title:
        errors['title'] = u"Ім'я є обов'язковим"
      else:
        data['title'] = title

      data['lat_title'] = time()
        
        
      price = request.POST.get('price', '').strip()
      if not price:
          errors['price'] = u"Ціна є обов'язковою"
      else:
          if is_digit(price) == 1:
            data['price'] = price
          else:
            errors['price'] = u"Введіть ціле число!"
      description = request.POST.get('description', '').strip()
      if not description:
        errors['description'] = u"Опис є обов'язковим"
      else:
        data['description'] = description  
      photo_main = request.FILES.get('photo_main')
      if not photo_main:
        errors['photo_main'] = u"Одне фото є обов'язковим"
      else:
        data['photo_main'] = photo_main 
      photo_big = request.FILES.get('photo_big')
      if photo_big:
        data['photo_big'] = photo_big 

           
      # save flovwer
      if not errors:
        flower = Flower(**data)
        flower.save()
        # redirect to students list
        return HttpResponseRedirect( u'%s?status_message=Квітку успішно додано!'  % reverse('main'))
      else:
        # render form with errors and previous user input
        return render(request, 'shop/flower_add.html',
        {'errors': errors})
    elif request.POST.get('cancel_button') is not None:
      # redirect to home page on cancel button
      return HttpResponseRedirect( u'%s?status_message=Додавання квітки скасовано!' % reverse('main'))
  else:
   # initial form render
   return render(request, 'shop/flower_add.html', {})




#####################################################################
#flower_edit


def flower_edit(request, pk):
    flower = Flower.objects.filter(pk=pk)

    
    if request.method == "POST":
        data = Flower.objects.get(pk=pk)
        if request.POST.get('add_button') is not None:
            
            errors = {}

            title = request.POST.get('title', '').strip()
            if not title:
                errors['title'] = u"Імʼя є обовʼязковим."
            else:
                data.title = title

            data.lat_title = time()

            price = request.POST.get('price', '').strip()
            if not price:
               errors['price'] = u"Ціна є обов'язковою"
            else:
               if is_digit(price) == 1:
                 data.price = price 
               else:
                 errors['price'] = u"Введіть ціле число!"

            description = request.POST.get('description', '').strip()
            if not description:
               errors['description'] = u"Опис є обов'язковим"
            else:
               data.description = description
            photo_main = request.FILES.get('photo_main')
            if not photo_main:
                errors['photo_main'] = u"Одне фото є обов'язковим"
            else:
                data.photo_main = photo_main 
            photo_big = request.FILES.get('photo_big')
            if photo_big:
               data.photo_big = photo_big 


            if errors:
                return render(request, 'shop/flower_edit.html', {'pk': pk, 'flower': data, 'errors': errors})
            else:
                data.save()
                return HttpResponseRedirect(u'%s?status_message=Редагування квітки  завершено' % reverse('main'))
        elif request.POST.get('cancel_button') is not None:

            return HttpResponseRedirect(u'%s?status_message=Редагування квітки скасовано!' % reverse('main'))
        
    else:
        return render(request,
                      'shop/flower_edit.html', {'pk': pk, 'flower': flower[0]})
                      
                      
                    






########################################

#flower delete

class FlowerDelete(DeleteView):
  model = Flower
  template_name = 'shop/flower_delete.html'
  def get_success_url(self):
    return u'%s?status_message=Квітку успішно видалено!' % reverse('main')
  def post(self, request, *args, **kwargs):
    if request.POST.get('no_delete_button'):
      return HttpResponseRedirect(u'%s?status_message=Видалення  квітки відмінено!'% reverse('main'))
    else:
      return super(FlowerDelete, self).post(request, *args, **kwargs)
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
        return super(FlowerDelete, self).dispatch(*args, **kwargs)




###############################################################################

def one_order(request, pk):
  order = Order.objects.filter(pk=pk)
  return render(request, 'shop/one_order.html', {'order':order})




