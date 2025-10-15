from django.urls import path
from polls import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
]
