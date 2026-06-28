from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('services/<slug:slug>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('projects/', views.ProjectsView.as_view(), name='projects'),
    path('projects/<slug:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('sustainability/', views.SustainabilityView.as_view(), name='sustainability'),
    path('gallery/', views.gallery, name='gallery'),
]
