from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = "ConvAI Admin"
admin.site.site_title = "ConvAI Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('learn/', views.learn, name='learn'),
    path('learn/<section_name>/', views.section_start, name='section_start'),
    path('about/', views.about, name='about'),
    path('send_message/', views.send_message, name='send_message'),
    path('clear/', views.clear, name='clear'),
    path('__reload__/', include('django_browser_reload.urls')),
]
