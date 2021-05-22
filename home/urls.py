from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('product/<int:p_id>/', views.product, name='product'),
    path('signup/', views.register_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('address/<int:p_id>/<int:buyer_id>/',views.placeOrder, name='placeOrder'),
]
