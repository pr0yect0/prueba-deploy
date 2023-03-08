from django.urls import path
from . import views
urlpatterns = [
    path('',views.wep_page, name='web_page'),
    path('usuarios',views.usuarios,name='usuarios'),
    path('cerrar_sesion/',views.cerrar_sesion,name='cerrar_sesion'),
    path('usuarios/<int:quote_id>/',views.del_quote,name='del_quote'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/<str:username>/', views.perfil, name='perfil'),
    path('update_user/', views.update_user,name='update_user')
    
]