
from django.contrib import admin
from django.urls import path, include
from tailwindapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Login,name='login'),
    path('signup/', views.SignupPage, name='signup'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('logout/', views.userlogout, name='logout'),
    path("__reload__/", include("django_browser_reload.urls")),
]

