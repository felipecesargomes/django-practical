from django.shortcuts import render

# Create your views here.
def index(request):
    print('blog')
    return HttpResponse('blog do app')