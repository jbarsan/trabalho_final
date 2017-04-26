from django.db import models

from django.utils import timezone
# Create your models here.


class Receita(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    tempo_preparo = models.TimeField(verbose_name='Tempo de preparo')
    rendimento = models.IntegerField(verbose_name='Rendimento')
    ingredientes = models.TextField()
    modo_preparo = models.TextField(verbose_name='Modo de preparo')
    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.data_publicacao = timezone.now()
        self.save()

    def aprovar_comentario(self):
        return self.comentarios.filter(comentario_aprovado=True) # Esse 'comentarios' é o related_name da variável 'receitas' na Classe 'Comentários'

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    receita = models.ForeignKey('blog.Receita', related_name='comentarios')
    autor = models.CharField(max_length=200)
    comentario = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    comentario_aprovado = models.BooleanField(default=False)

    def aprovar(self):
        self.comentario_aprovado = True
        self.save()

    def __str__(self):
        return self.comentario