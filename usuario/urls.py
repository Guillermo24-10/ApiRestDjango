from django.urls import path
from .views import UsuarioList

urlpatterns =[
    path('usuario', UsuarioList.as_view(),name='Usuario_List')
]