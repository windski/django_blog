from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
import logging

from .models import Article


# Create your views here.

def index(request):
    latest_article_list = Article.objects.order_by('-date')[:5]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'blog/blog.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/detail.html', {'article': article})


def results(request, article_id):
    response = "You're looing at the results of question %s."
    return HttpResponse(response % article_id)

def submit(request, article_id):
    pass


def login(request):
    if request.method == 'GET':
        return render(request, 'blog/login.html')
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponse('Ok!')
        else:
            return render(request, 'blog/login.html', {'error': True})



def register(request):
    return render(request, 'blog/register.html')


@login_required
def account(request):
    pass
