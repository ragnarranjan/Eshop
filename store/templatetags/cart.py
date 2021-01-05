from django import template

register =  template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product , cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:  #if we will go for >> if id == product.id --id is str type product id is str so it will give false .
            return True
    return False;








    