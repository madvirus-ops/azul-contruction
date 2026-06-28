from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.dashboard_login, name='dashboard_login'),
    path('logout/', views.dashboard_logout, name='dashboard_logout'),
    path('', views.dashboard_home, name='dashboard_home'),

    # Services
    path('services/', views.service_list, name='dashboard_services'),
    path('services/add/', views.service_create, name='dashboard_service_create'),
    path('services/<int:pk>/edit/', views.service_edit, name='dashboard_service_edit'),
    path('services/<int:pk>/delete/', views.service_delete, name='dashboard_service_delete'),

    # Projects
    path('projects/', views.project_list, name='dashboard_projects'),
    path('projects/add/', views.project_create, name='dashboard_project_create'),
    path('projects/<int:pk>/edit/', views.project_edit, name='dashboard_project_edit'),
    path('projects/<int:pk>/delete/', views.project_delete, name='dashboard_project_delete'),
    path('projects/<int:project_pk>/images/add/', views.project_image_add, name='dashboard_project_image_add'),
    path('projects/images/<int:pk>/delete/', views.project_image_delete, name='dashboard_project_image_delete'),

    # Gallery
    path('gallery/', views.gallery_list, name='dashboard_gallery'),
    path('gallery/add/', views.gallery_create, name='dashboard_gallery_create'),
    path('gallery/bulk/', views.gallery_bulk_upload, name='dashboard_gallery_bulk'),
    path('gallery/<int:pk>/edit/', views.gallery_edit, name='dashboard_gallery_edit'),
    path('gallery/<int:pk>/delete/', views.gallery_delete, name='dashboard_gallery_delete'),

    # Stats
    path('stats/', views.stat_list, name='dashboard_stats'),
    path('stats/add/', views.stat_create, name='dashboard_stat_create'),
    path('stats/<int:pk>/edit/', views.stat_edit, name='dashboard_stat_edit'),
    path('stats/<int:pk>/delete/', views.stat_delete, name='dashboard_stat_delete'),

    # Company Info
    path('company/', views.company_edit, name='dashboard_company'),

    # Sustainability
    path('sustainability/', views.sustainability_list, name='dashboard_sustainability'),
    path('sustainability/add/', views.sustainability_create, name='dashboard_sustainability_create'),
    path('sustainability/<int:pk>/edit/', views.sustainability_edit, name='dashboard_sustainability_edit'),
    path('sustainability/<int:pk>/delete/', views.sustainability_delete, name='dashboard_sustainability_delete'),

    # Contact Messages
    path('messages/', views.contact_messages, name='dashboard_contact_messages'),
    path('messages/<int:pk>/', views.contact_message_detail, name='dashboard_contact_message_detail'),
    path('messages/<int:pk>/delete/', views.contact_message_delete, name='dashboard_contact_message_delete'),
]
