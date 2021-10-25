from django.urls import path

from app.views import dc_hero_list_by_50 , dc_hero_details , dc_hero_create , dc_hero_full_update   ,dc_hero_partial_update ,  dc_hero_delete 



app_name = 'app'

urlpatterns = [
    
    path('list/', dc_hero_list_by_50, name="lista"),
    path('details/<int:hero>/', dc_hero_details, name="detalhes"),
    path('create/', dc_hero_create, name="adicionar"),
    path('update/<int:hero>/', dc_hero_full_update, name="atualizar"),
    path('partial/<int:hero>/', dc_hero_partial_update, name="atualizar parcialmente"),
    path('delete/<int:hero>/', dc_hero_delete, name="deletetar"),
   
   
]