from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models. customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View


class Login(View):
    def get(self,request):
        return render(request,'orders/login.html')

    def post(self,request):
        email = request.POST.get('email') #we will use this email in index.html to print the logeedin user name
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password,customer.password)
            if flag == True:
                request.session ['customer'] = customer.id #this line or request.session ['customer_id'] = customer.id  --are same
                #request.session ['customer_id'] = customer.id # in customer obj every inform is available 
                #request.session['email'] = customer.email
                return redirect ('homepage')
            else:
                error_message = 'email or password invalid'
        print(email,password)
        return render(request,'orders/login.html',{'error' : error_message})


def logout(request):
    request.session.clear()
    return redirect('login')