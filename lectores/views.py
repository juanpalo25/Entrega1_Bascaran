from ast import Return
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import Context, Template, loader
from lectores.forms import Busqueda_blog, FormBlog
from lectores.models import Blog
from datetime import datetime


def home(request):
    return render(request, 'index.html')

def crear_blog(request):
    
    #print(request.GET)
    #titulo = request.GET.get('titulo')
    #caracteres = request.POST.get("caracteres")
    #fecha_creacion = request.POST.get()
    #genero = request.POST.get('genero')
    #autor = request.POST.get('autor')
    
    #blog = Blog(titulo=titulo, caracteres=caracteres, fecha_creacion = datetime.now(), genero=genero, autor=autor)
    #blog.save()
    if request.method == 'POST':
        form = FormBlog(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            fecha = data.get('fecha_creacion')
            blog = Blog(titulo=data.get('titulo'), caracteres=data.get('caracteres'), fecha_creacion = fecha if fecha else datetime.now(), genero=data.get('genero'), autor=data.get('autor'))
            blog.save()
            listado_blogs = Blog.objects.all
            return redirect('listado_blogs')
        else: return render(request, 'blogs/crear_blog.html',{'form': form})
    form_blog = FormBlog()

    return render(request, 'blogs/crear_blog.html',{'form': form_blog})

def listado_blogs(request):
    
    titulo_busqueda = request.GET.get('titulo')

    if titulo_busqueda:
        listado_blogs = Blog.objects.filter(titulo__icontains= titulo_busqueda)
    else:
        listado_blogs = Blog.objects.all()
        
    form = Busqueda_blog()
    return render(request, 'blogs/listado_blogs.html', {'blogs/listado_blogs': listado_blogs, 'form':form})

def vista_base(request):
    return render(request, 'base.html')

def editar_blog(request, id):
    blog = Blog.objects.get(id = id)

    if request.method == 'POST':
        form = FormBlog(request.POST)
        if form.is_valid():
            blog = Blog.objects.get(id = id)    
            blog.titulo = form.cleaned_data.get('titulo')
            blog.caracteres = form.cleaned_data.get('caracteres')
            blog.fecha_creacion = form.cleaned_data.get('fecha_creacion')
            blog.genero = form.cleaned_data.get('genero')
            blog.autor = form.cleaned_data.get('autor')
            blog.save()
            return redirect('listado_blogs')
        else: 
            return render(request, 'blogs/editar_blog.html',{'form': form, 'blog':blog})
    form_blog = FormBlog(initial={'titulo': blog.titulo, 'caracteres': blog.caracteres, 'fecha_creacion':blog.fecha_creacion, 'genero': blog.genero, 'autor': blog.autor})
    return render(request, 'blogs/editar_blog.html', {'form': form_blog, 'blog': blog} )


def eliminar_blog(request, id):
    blog =Blog.objects.get(id = id)
    blog.delete()
     
    return redirect('listado_blogs')

def mostrar_blog(request, id):
    blog = Blog.objects.get(id = id)
    return render(request, 'blogs/mostrar_blog.html', {'blog': blog})