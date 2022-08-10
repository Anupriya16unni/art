 
from django.shortcuts import redirect, render
from artist_app.models import *
from .models import *
from user_app.models import *
from django.http import JsonResponse


# Create your views here.

def contact (request):
    if request.method=="POST":
        current_user=request.session['user_id']
        contact=ArtUser.objects.get(id=current_user)

        contact_name=request.POST["c_name"]
        contact_email=request.POST['c_email']
        contact_message=request.POST["c_msg"]
        
        obj=ContactUs(name=contact_name,email=contact_email,message=contact_message,contact_id=contact)
        obj.save()
    return render (request,'userapp/contact.html')

def login (request):
    error=''
    if request.method=='POST':
        user_email=request.POST['email']
        user_pass=request.POST['pass']
        try:
            user_data=ArtUser.objects.get(email=user_email,password=user_pass)
            request.session['user_id']=user_data.id
            return redirect('home')
        except:
            error="invalid email id or password"
    return render (request,'userapp/login.html',{'error':error})

def signup (request):
    data=""
    if request.method=="POST":
        user_fname=request.POST["fname"]
        user_lname=request.POST["lname"]
        user_address=request.POST["address"]
        user_gender=request.POST["gender"]
        user_email=request.POST['email']
        user_password=request.POST['pass']
            
        obj=ArtUser(fname=user_fname,lname=user_lname,address=user_address,gender=user_gender,email=user_email,password=user_password)
        obj.save()
        data="successfully registered"
    return render (request,'userapp/signup.html',{'data':data})

def about (request):
    return render (request,'userapp/about.html')

def home (request):
    prof_details=""
    if 'user_id' in request.session:
        current_user=request.session['user_id']
        prof_details=ArtUser.objects.get(id=current_user)
        return render (request,'userapp/home.html',{'prof':prof_details, 'status': current_user})
    return render (request,'userapp/home.html')

def drawing (request):
    return render (request,'userapp/drawing.html')

def user_profile (request):
    return render (request,'userapp/user_profile.html')

def user_login_security (request):
    return render (request,'userapp/user_login_security.html')

def user_address (request):
    return render (request,'userapp/user_address.html')   

def logout (request):
    del request.session['user_id']
    request.session.flush()
    return render (request,'userapp/logout.html')

def add_cart (request,pid):
    product=Product.objects.get(id=pid)
    sid = request.session['user_id']
    user=ArtUser.objects.get(id= sid)
    cart_exist=Cart.objects.filter(product=pid,user=request.session['user_id']).exists()
    if not cart_exist:
        cart=Cart(product=product,user=user)
        cart.save()
    return redirect('home')

def view_cart (request):
    cart_product=Cart.objects.filter(user=request.session['user_id'])
    return render (request,'userapp/view_cart.html',{"cart_product":cart_product})

def delete_cart (request):
    id=request.POST['pid']
    prod=Cart.objects.get(product=id,user=request.session['user_id'])
    prod.delete()
    return redirect('view_cart')

def artist_details (request):
    return render (request,'userapp/artist_details.html')

def forgot_password (request):
    message=''
    if request.method=='POST':
        old_pass=request.POST['old']
        new_pass=request.POST['new']
        cnfrm_pass=request.POST['cnfrm']
        data=ArtUser.objects.get(id=request.session['user_id'])
        if data.password==old_pass:
            if new_pass==cnfrm_pass:
                data.password=new_pass
                data.save()
                message="password change successfully"
            else:
                message="password does not match"
        else:
            message="password incorrect"
    return render (request,'userapp/forgot_password.html',{"msg":message}) 

def ToDraw (request):
    return render (request,'userapp/to_draw.html')

def show_product (request):
    products=Product.objects.all()
    return render (request,'userapp/show_product.html',{"product":products})