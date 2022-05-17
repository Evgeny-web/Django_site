from django import template
from Hotel.models import *

register = template.Library()


@register.simple_tag()
def get_type_rooms():
    return Type.objects.all()


@register.simple_tag(name='getrooms')
def get_rooms():
    return Room.objects.all()


@register.inclusion_tag('Hotel/List_paymethod.html')
def get_pay_method(filter=None):
    if not filter:
        paymets = PayMethod.objects.all()
    else:
        paymets = PayMethod.objects.filter(pay_type=filter)

    return {'paymets': paymets}