from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts':posts})

def category(request, category_id):
    # buscar por id, si no existe: 404
    category = get_object_or_404(Category, id = category_id)
    # posts filtrados por categoría
    posts = Post.objects.filter(categories=category)

    # la parte de arriba es una manera de hacerlo, pero se puede hacer con 'related_name' en models
    return render(request, 'blog/category.html', { 'category':category, 'posts':posts })