# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Flower
from .models import Order


admin.site.register(Flower)
admin.site.register(Order)


