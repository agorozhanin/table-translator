from django.urls import path

from main.views import DeclarationApiView, index, update_table

urlpatterns = [
    path('api/save-declarations', DeclarationApiView.as_view()),
    path('', index, name = 'index'),
    path('update_table', update_table, name='update_table'),
]
