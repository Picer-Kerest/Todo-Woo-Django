from django.template.base import TemplateSyntaxError

# -*- coding: utf-8 -*-

# Стандартный импорт библиотеки шаблонов
from django import template

# Это чтобы register.filter работал
register = template.Library()

@register.filter
def rupluralize(value, endings='задача, задачи, задач'):
    try:
        endings = endings.split(',')
        if value % 100 in (11, 12, 13, 14):
            return endings[2]
        if value % 10 == 1:
            return endings[0]
        if value % 10 in (2, 3, 4):
            return endings[1]
        else:
            return endings[2]
    except:
        raise TemplateSyntaxError