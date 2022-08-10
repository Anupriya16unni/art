from unicodedata import category
from django.shortcuts import render,redirect

from artist_app.models import Artist, Product
from user_app.models import ArtUser
from user_app.views import about

# Create your views here.

def addstock (request):
    if request.method=='POST':
        p_name=request.POST['p_name']
        p_desc=request.POST['p_desc']
        p_price=request.POST['p_price']
        p_stock=request.POST['p_stock'] 
        p_img=request.FILES['p_img']

        prod=Product(product_name=p_name,desc=p_desc,stock=p_stock,image=p_img,price=p_price)
        prod.save()
    return render (request,'artistapp/addstock.html')

def register (request):
    suc=""
    if request.method=="POST":
        artist_name=request.POST["a_name"]
        artist_email=request.POST['a_email']
        artist_password=request.POST['a_password']
        artist_qualification=request.POST["a_qualification"]
        artist_category=request.POST["a_category"]
        artist_about=request.POST["a_about"]

        obj=Artist(name=artist_name,email=artist_email,password=artist_password,qualification=artist_qualification,category=artist_category,about=artist_about)
        obj.save()
        suc="successfully registered"
    return render (request,'artistapp/register.html', {"data":suc} )

def artist_profile (request):
    return render (request,'artistapp/artist_profile.html')
    
def view_stock (request):
    products=Product.objects.all()
    return render (request,'artistapp/view_stock.html',{"product":products})

def login_security (request):
    prof=Artist.objects.get(id=request.session['artist_id'])
    return render (request,'artistapp/login_security.html',{'prof':prof})

def artist_home (request):
    current_artist=request.session['artist_id']
    prof_details=Artist.objects.get(id=current_artist)
    return render (request,'artistapp/artist_home.html',{'prof':prof_details})

def artist_login (request):
    error=''
    if request.method=='POST':
        artist_email=request.POST['email']
        artist_pass=request.POST['pass']
        try:
            artist_data=Artist.objects.get(email=artist_email,password=artist_pass)
            approve = artist_data.approved
            if approve == 'approved':
                request.session['artist_id']=artist_data.id
                return redirect('artist:artist_home')
            else:
                error1="admin should approve"
                return render (request,'artistapp/artist_login.html',{'error1':error1})
        except:
            error="invalid email id or password"
    return render (request,'artistapp/artist_login.html',{'error':error})

def order_management (request):
    return render (request,'artistapp/order_management.html')

def artist_logout (request):
    return render (request,'artistapp/artist_logout.html')

def change_password (request):
    message=''
    if request.method=='POST':
        old_pass=request.POST['old']
        new_pass=request.POST['new']
        cnfrm_pass=request.POST['cnfrm']
        data=Artist.objects.get(id=request.session['artist_id'])
        if data.password==old_pass:
            if new_pass==cnfrm_pass:
                data.password=new_pass
                data.save()
                message="password change successfully"
            else:
                message="password does not match"
        else:
            message="password incorrect"
    return render (request,'artistapp/change_password.html',{"msg":message})

def address (request):
    return render (request,'artistapp/address.html') 
