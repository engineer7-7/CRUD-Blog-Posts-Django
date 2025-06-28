from django.urls import path
from .views import display_page, display_projects, contact, index

urlpatterns = [
    path('about/', display_page, name='about_page'),
    path('projects/', display_projects, name='display_projects'),
    path('contact/', contact, name='contact'),
    path('', index, name='index')
]
