from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('place_order/', views.place_order, name='place_order'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login.html'), name='logout'),
    path('delivery/', views.delivery , name='delivery'),
    path('app_details/', views.app_details, name='app_details'),

]