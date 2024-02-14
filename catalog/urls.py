from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import register
from django.contrib.auth.views import LoginView, LogoutView

app_name="catalog"
urlpatterns = [
	 path("", views.IndexView.as_view(), name="index"),
	 path("<int:pk>/", views.DetailView.as_view(), name="detail"),
	 path("<int:cat_id>/schedulevisit", views.schedulevisit, name="schedulevisit"),
	 path("<int:pk>/confirmation", views.ConfirmationView.as_view(), name="confirmation"),
	 path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),



]
