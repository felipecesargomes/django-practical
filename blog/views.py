from django.shortcuts import render

# Create your views here.

def blog(request):
    print('blog')
    return render(
        request,
        'blog/index.html', {'range': range(7)}
    )

def exemplo(request):
    print('exemplo')
    return render(
        request,
        'blog/exemplo.html'
    )
