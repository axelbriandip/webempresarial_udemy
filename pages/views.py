from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.
def page(request, page_id, page_title):
    # buscar por id, si no existe: 404
    page = get_object_or_404(Page, id = page_id)

    # la parte de arriba es una manera de hacerlo, pero se puede hacer con 'related_name' en models
    return render(request, 'pages/sample.html', { 'page': page })