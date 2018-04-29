from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
import logging

from .models import Article, NewUser


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
            url = '/account/' + username
            return redirect(url)
        else:
            return render(request, 'blog/login.html', {'error': True})



def register(request):
    if request.method == 'GET':
        return render(request, 'blog/register.html')
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')
        if password1 != password2:
            return render(request, 'blog/register.html', {'notequal': True, 'userexist': False})

        try:
            user = NewUser.objects.get(username=username)
        except ObjectDoesNotExist:
            user = NewUser(username=username, email=email)
            user.set_password(password1)
            user.save()
            return redirect('/login/')
        else:
            return render(request, 'blog/register.html', {'userexist': True, 'notequal': False})


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')


@login_required
def account(request, username):
    return HttpResponse("user account page!\nhello, " + username)


def about_me(request):
    return render(request, 'blog/about_me.html')
