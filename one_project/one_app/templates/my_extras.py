from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value, args):
    """"
    this cuts out all "args" from the value.
    """
    return value.replace(args, '')

#register.filter("cut", cut)