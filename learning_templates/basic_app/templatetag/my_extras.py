from django import template

register = template.library()
@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts out all value of 'arg' from the string
    """

    return value.replace(arg,'')

register.filter('cut',cut)
