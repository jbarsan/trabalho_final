from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
# Create your views here.


def receita_detalhe(request, pk):
    receita = get_object_or_404(Receita, pk=pk)
    return render(request, 'blog/receita_detalhe.html', {'receita': receita})


def receita_lista(request):
    receitas = Receita.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'blog/receita_lista.html', {'receitas': receitas})


@login_required
def nova_receita(request):
    if request.method == 'POST':
        formulario = ReceitaForm(request.POST)
        if formulario.is_valid():
            receita = formulario.save(commit=False)
            receita.autor = request.user
            #receita.data_publicacao = timezone.now()
            receita.save()
            return redirect('blog:receita_detalhe', pk=receita.pk)
    else:
        formulario = ReceitaForm()
    return render(request, 'blog/editar_receita.html', {'formulario': formulario})


@login_required
def editar_receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)
    if request.method == "POST":
        formulario = ReceitaForm(request.POST, instance=receita)
        if formulario.is_valid():
            receita = formulario.save(commit=False)
            receita.autor = request.user
            receita.published_date = timezone.now()
            receita.save()
            return redirect('blog:post_detail', pk=receita.pk)
    else:
        formulario = ReceitaForm(instance=receita)
    return render(request, 'blog/editar_receita.html', {'formulario': formulario})


@login_required
def rascunhos(request):
    receitas = Receita.objects.filter(data_publicacao__isnull=True).order_by('data_criacao')
    return render(request, 'blog/rascunhos.html', {'receitas': receitas})


@login_required
def publicar_receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)
    receita.publicar()
    return redirect("blog:receita_detalhe", pk=receita.pk)


@login_required
def remover_receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)
    receita.delete()
    return redirect('blog:receita_lista')


def add_comentario_a_receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)
    if request.method == 'POST':
        formulario = ComentarioForm(request.POST)
        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.receita = receita
            comentario.save()
            return redirect('blog:receita_detalhe', pk=receita.pk)
    else:
        formulario = ComentarioForm()
    return render(request, 'blog/add_comentario_a_receita.html', {'formulario': formulario})


@login_required
def aprovar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario.aprovar()
    return redirect('blog:receita_detalhe', pk=comentario.receita.pk)


@login_required
def remover_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario.delete()
    return redirect('blog:receita_detalhe', pk=comentario.receita.pk)


def mostra_todas(request):
    receitas = Receita.objects.all()
    titulos = []
    for titulo in receitas:
        titulos.append(titulo.titulo)
    return titulos
