from django import template
register = template.Library()

print 'register div'
@register.filter(name='ratioWidth')
def ratioWidth( value, arg ):
    '''
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    '''
    try:
        value = float( value )
        arg = float( arg )
        if arg: 
            return ((value / arg) <= (3.0/2.0))
    except: pass
    return ''