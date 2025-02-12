from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Landing page
    path('get-started/', views.get_started, name='get_started'),  # Get Started page
    path('meal-plan/', views.meal_plan, name='meal_plan'),  # Meal plan page
    path('signup/',views.signup,name='signup'),
]
