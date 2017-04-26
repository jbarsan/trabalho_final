from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.receita_lista, name='receita_lista'),
    url(r'^receita/(?P<pk>[0-9]+)/$', views.receita_detalhe, name='receita_detalhe'),
    url(r'^receita/new/$', views.nova_receita, name='nova_receita'),
    url(r'^receita/(?P<pk>[0-9]+)/editar/$', views.editar_receita, name='editar_receita'),
    url(r'^receita/(?P<pk>\d+)/publicar/$', views.publicar_receita, name='publicar_receita'),
    url(r'^receita/(?P<pk>\d+)/remover/$', views.remover_receita, name='remover_receita'),
    url(r'^receita/(?P<pk>\d+)/comentario/$', views.add_comentario_a_receita, name='add_comentario_a_receita'),
    url(r'^rascunhos/$', views.rascunhos, name='rascunhos'),
    url(r'^comentario/(?P<pk>\d+)/aprovar/$', views.aprovar_comentario, name='aprovar_comentario'),
    url(r'^comentario/(?P<pk>\d+)/remover/$', views.remover_comentario, name='remover_comentario'),
]