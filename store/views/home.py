from django.shortcuts import render,redirect,HttpResponse
from store.models.product import Product
from store.models.category import Category
from django.views import View


class Index(View):

    def post(self,request):
        product = request.POST.get('product')  #to get productid----we can read 
        cart = request.session.get('cart')
        print(product)             
        return redirect('homepage')


    def get(self,request):        
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();
            
        data = {}
        data['products'] = products
        data['categories'] = categories
        return render(request, 'orders/index.html', data)
        


""" def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')  #storing category like 1 or 2  means if 1 men else 2 women  here category is coming from for loop in html ------for category in categories
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();
    data = {}
    data['products'] = products
    data['categories'] = categories
    print('yours email is',request.session.get('email'))
    return render(request, 'orders/index.html', data) """



""" def signup(request):
    if request.method=='GET':
        return render(request,'orders/signup.html')
    else:
        return registerUser(request)
 """     

"""def registerUser(request):
    postdata = request.POST
    first_name = postdata.get('first_name')
    last_name = postdata.get('last_name')
    email = postdata.get('email')
    phone = postdata.get('phone')
    password = postdata.get('password')

    value = {
        'first_name' : first_name,
        'last_name' : last_name,
        'email' : email,
        'phone' : phone
    }
    error_message = None
    
    customer = Customer(first_name = first_name,   #here we r creating obj and storing.
                        last_name = last_name,
                        phone = phone,
                        email = email,
                        password = password )

    error_message = validateCustomer(customer) 

    if not error_message:
        customer.password = make_password(customer.password)
        customer.register()  #customer.save() or we can directly store the data like this step
        return redirect("homepage")   ## or we can also make a func & can save  
    else:                   
        data = { 
            'error' : error_message,
            'values' : value 
        }                   
        return render(request,"orders/signup.html",data ) """



""" def validateCustomer(customer):
    error_message = None
    if (not customer.first_name):
        error_message = "First Name Required !!"
    elif len(customer.first_name) < 4:
        error_message = 'First Name must be 4 char long or more'
    elif not customer.last_name:
        error_message = 'Last Name Required'
    elif len(customer.last_name) < 4:
        error_message = 'Last Name must be 4 char long or more'
    elif not customer.phone:
        error_message = 'Phone Number required'
    elif len(customer.phone) < 10:
        error_message = 'Phone Number must be 10 char Long'
    elif len(customer.password) < 6:
        error_message = 'Password must be 6 char long'
    elif len(customer.email) < 5:
        error_message = 'Email must be 5 char long'
    elif customer.isExists():
        error_message = 'Email Address Already Registered..'

    return error_message
 """
   

""" def login(request):
    if request.method=='GET':
        return render(request,'orders/login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password,customer.password)
            if flag == True:
                return redirect ('homepage')
            else:
                error_message = 'email or password invalid'
        print(email,password)
        return render(request,'orders/login.html',{'error' : error_message})
         """