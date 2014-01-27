from django import template

register = template.Library()

@register.simple_tag
def get_rgba_from_hex(value, opacity):
    value = value.lstrip('#')
    lv = len(value)
    strTuple = "rgba"+''.join(str(tuple(int(value[i:i+lv/3], 16) for i in
                                        range(0, lv, lv/3))))[:-1]+", "+str(opacity)+")"
    return strTuple