from django.shortcuts import render

# Create your views here.

def blog(request):
    context_blog = {
        'text': 'Bem vindo ao Blog',
        'range': range(7)
    }
    print('blog')
    return render(
        request,
        'blog/index.html', 
        context_blog
    )

def exemplo(request):
    context_exemplo = {
        'text': 'Exemplo'
    }
    print('exemplo')
    return render(
        request,
        'blog/exemplo.html',
        context_exemplo
    )
