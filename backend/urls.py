from django.urls import path
from .views import home, single, about

app_name = 'blog'

urlpatterns = [
    path('home/', home, name = 'homepage' ),
    path('single/<slug:slug>', single, name = 'single'),
    path('about/', about, name = 'about')
] 
