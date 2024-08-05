from django.urls import path
from.import views


urlpatterns = [
   path('cliente/', views.cliente,name='cliente'),
   path('agendamento/', views.agendamento,name='agendamento'),
   path('servicos/', views.servicos,name='servicos'),
   path('area/', views.area,name='area'),
   path('area_servicos/', views.area_servicos,name='area_servicos'),
   path('area_clientes/', views.area_clientes,name='area_clientes'),
   path('cliente_add/', views.cliente_add,name='cliente_add')
   
   
]
   
