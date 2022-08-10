from django.urls import path
from .import views

urlpatterns =[

    path('message',views.message,name="message"),
    path('reply/<int:id>',views.reply,name="reply"),
    path('artist_request',views.artist_request,name="artist_request"),
    path('admin_profile',views.admin_profile,name="admin_profile"),
    path('admin_logout',views.admin_logout,name="admin_logout"),
    path('admin_home',views.admin_home,name="admin_home"),
    path('artist_info',views.artist_info,name="artist_info"),
    path('customer_info',views.customer_info,name="customer_info"),
    path('',views.admin_login,name="admin_login")
    
]