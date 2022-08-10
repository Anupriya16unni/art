from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [

    path('contact', views.contact, name="contact"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('about', views.about, name="about"),
    path('', views.home, name="home"),
    path('drawing', views.drawing, name="drawing"),
    path('user_profile', views.user_profile, name="user_profile"),
    path('user_login_security', views.user_login_security, name="user_login_security"),
    path('user_address', views.user_address, name="user_address"),
    path('cart/<int:pid>',views.add_cart,name="addToCart"),
    path('cart',views.view_cart,name="view_cart"),
    path('logout', views.logout, name="logout"),
    path('delete_cart',views.delete_cart,name="delete_cart"),
    path('forgot_password',views.forgot_password,name="forgot_password"),
    path('artist_details', views.artist_details, name="artist_details"),
    path('show_product', views.show_product, name="show_product"),
    path('toDraw', views.ToDraw, name="toDraw")
]
