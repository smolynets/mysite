# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Flower(models.Model):

	class Meta(object):
		verbose_name = u'Квітка'
		verbose_name_plural = u'Квіти'

	title = models.CharField(
      max_length=256,
      blank=False)
	lat_title = models.CharField(
      max_length=256,
      blank=False)
	price = models.CharField(
      max_length=256,
      blank=False)
	description = models.TextField(
      blank=False)
	photo_main = models.ImageField(
      blank=False,
      null=False)
	photo_big = models.ImageField(
      blank=True,
      null=True)
	def __unicode__(self):
		return u'%s' % (self.title)





class Order(models.Model):

	class Meta(object):
		verbose_name = u'Замовлення'
		verbose_name_plural = u'Замовлення'

	name = models.CharField(
      max_length=256,
      blank=False)
	number = models.CharField(
      max_length=256,
      blank=False)
	syma = models.CharField(
      max_length=256,
      blank=False)
	body = models.TextField(
      blank=True)
	notes = models.TextField(
      blank=True)
	def __unicode__(self):
		return u'%s' % (self.name)
    
      


