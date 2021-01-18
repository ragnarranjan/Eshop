from django import template
register =  template.Library()


@register.filter(name = 'is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:  #if we will go for >> if id == product.id --id is str type product id is str so it will give false .
            return True
    return False


@register.filter(name = 'cart_quantity')
def cart_quantity(product,cart):
    print("-------------------->"*20)
    keys = cart.keys()
    for id in keys:
        print("(((((", id, product.id)
        if int(id) == product.id:  #if we will go for >> if id == product.id --id is str type product id is str so it will give false .
            print("---------------------------------****", cart.get(id))
            
            return cart.get(id)  #by cart.get(id) we r getting no of items in cart bcz get will give vallue associated with key-id 
    return 0






    