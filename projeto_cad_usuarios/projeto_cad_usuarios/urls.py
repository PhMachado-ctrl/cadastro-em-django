
from django.urls import path
from cad_users import views

urlpatterns = [
   # rota, view responsável, nome de referência
   #Página Principal
   path('',views.home, name='home'),
]
