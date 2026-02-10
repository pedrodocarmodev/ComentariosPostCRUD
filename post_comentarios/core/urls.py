from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.post, name='post'),
    path('add-comentario/<int:post_id>/', views.add_comentario, name='add_comentario'),
    path('deletar-comentario/<int:post_id>/<int:id>/', views.deletar_comentario, name='deletar_comentario'),
]