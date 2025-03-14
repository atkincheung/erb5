from django.urls import path
from . import views
urlpatterns = [
    path('contact', views.contact, name='contact')
]
# Compare this snippet from contacts/views.py: