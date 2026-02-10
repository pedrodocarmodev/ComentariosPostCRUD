from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comentario

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'index.html', {'posts' : posts})

def post(request, id):
    post = Post.objects.get(id = id)
    comentarios = Comentario.objects.filter(post_id=id).order_by('-id')
    return render(request, 'post.html', {'post' : post, 'comentarios' : comentarios})

def add_comentario(request, post_id):
    texto = request.POST.get('texto')
    comentario = Comentario(post_id=post_id, texto=texto)
    comentario.save()

    return redirect(f'/post/{post_id}')

def deletar_comentario(request, post_id, id):
    comentario = Comentario.objects.get(id = id)
    comentario.delete()

    return redirect(f'/post/{post_id}')