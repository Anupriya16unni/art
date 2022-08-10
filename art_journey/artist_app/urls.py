from django.urls import path
from .import views
app_name="artist"

urlpatterns =[

    path('addstock',views.addstock,name="addstock"),
    path('register',views.register,name="register"),
    path('artist_profile',views.artist_profile,name="artist_profile"),
    path('view_stock',views.view_stock,name="view_stock"),
    path('login_security',views.login_security,name="login_security"),
    path('artist_home',views.artist_home,name="artist_home"),
    path('',views.artist_login,name="artist_login"),
    path('order_management',views.order_management,name="order_management"),
    path('artist_logout',views.artist_logout,name="artist_logout"),
    path('change_password',views.change_password,name="change_password"),
    path('address', views.address, name="address")

    
]