from cmath import e
from django.shortcuts import render,redirect

from admin_app.models import AdminLogin, AdminProfile
from artist_app.models import Artist
import user_app.models
from django.core.mail import send_mail
from django.conf import settings




# Create your views here.
def message (request):
    contact=user_app.models.ContactUs.objects.all()
    return render (request,'adminapp/message.html',{'contact':contact})

def reply (request,id):
    contact=user_app.models.ContactUs.objects.get(id=id)
    if request.method=="POST":
        contact.reply=request.POST['rply']
        contact.save()
    return render (request,'adminapp/reply.html',{'contact':contact})

def artist_request (request):
    artist_request=Artist.objects.filter(approved='not approved')
    if request.method=='POST':
        selected_req=Artist.objects.get(id=request.POST['id'])
        if 'approve' in request.POST:
            subject='email verifivation'
            message='Hi your account has been approved by Admin, Now you can login to the system'
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[selected_req.email]
            send_mail(subject,message,email_from,recipient_list)
            selected_req.approved='approved'
        if 'reject' in request.POST:
            subject='email verifivation'
            message='Hi your account has been rejected by Admin, so you not login to the system'
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[selected_req.email]
            send_mail(subject,message,email_from,recipient_list)
            selected_req.approved='rejected'
        selected_req.save()
    return render (request,'adminapp/artist_request.html',{'artist':artist_request})

def admin_profile (request):
    current_admin=request.session['admin_id']
    profile_name=AdminLogin.objects.get(id=current_admin)
    if request.method=="POST":
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        admin_email=request.POST['a_email']
        gender=request.POST["gender"]
        address=request.POST["address"]
        

        obj=AdminProfile(firstname=fname,lastname=lname,email=admin_email,gender=gender,address=address)
        obj.save()
    return render (request,'adminapp/admin_profile.html',{'profile':profile_name})

def admin_logout (request):
    return render (request,'adminapp/admin_logout.html')

def admin_home (request):
    current_admin=request.session['admin_id']
    profile_details=AdminLogin.objects.get(id=current_admin)
    return render (request,'adminapp/admin_home.html',{'profile':profile_details})

def artist_info (request):
    artist_request=Artist.objects.filter(approved='approved')
    return render (request,'adminapp/artist_info.html',{'artist':artist_request})

def customer_info (request):
    user=user_app.models.ArtUser.objects.all()
    return render (request,'adminapp/customer_info.html',{'user':user})

def admin_login (request):
    error=''
    if request.method=='POST':
        admin_name=request.POST['uname']
        admin_pass=request.POST['pass']
        try:
            admin_data=AdminLogin.objects.get(username=admin_name,password=admin_pass)
            request.session['admin_id']=admin_data.id
            return redirect('admin_home')
        except:
            error="invalid username or password"
    return render (request,'adminapp/admin_login.html',{'error':error})


