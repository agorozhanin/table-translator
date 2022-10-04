from django.urls import path

from main.views import DeclarationApiView

urlpatterns = [
    path('api/save-declarations', DeclarationApiView.as_view())
]
