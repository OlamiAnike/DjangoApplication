from django.urls import path
from . import views

app_name = "register"   


urlpatterns = [
    path('', views.homepage, name='home'),
    path("password_reset", views.password_reset_request, name="password_reset"),
]