from django.urls import path
from . import views

urlpatterns = [
    path('authenticated/endpoint', views.lockedEndpointView.as_view(), name='lockedEndpoint'),
]
